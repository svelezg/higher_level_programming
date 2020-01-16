#!/usr/bin/python3
"""
takes in 3 strings and sends a search request to the Twitter API
"""
import requests
import sys
import base64

if __name__ == "__main__":
    """The first argument must be the Consumer Key (API Key)"""
    API_key = sys.argv[1]
    """The second argument must be the Consumer Secret (API Secret)"""
    API_secret = sys.argv[2]
    """The third argument must be the search string"""
    search_string = sys.argv[3]

    key_secret = '{}:{}'.format(API_key, API_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }

    auth_data = {'grant_type': 'client_credentials'}
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    access_token = auth_resp.json()['access_token']

    search_headers = {'Authorization': 'Bearer {}'.format(access_token)}
    search_params = {
        'q': search_string,
        'result_type': 'recent',
        'count': 5
    }

    search_url = '{}1.1/search/tweets.json'.format(base_url)
    search_resp = requests.get(search_url, headers=search_headers,
                               params=search_params)

    for tweet in search_resp.get("statuses"):
        print("[{}] {} by {}".format(tweet.get("id"),
                                     tweet.get("text"),
                                     tweet.get("user").get("name")))
