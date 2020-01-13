#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        print("{}".format(response.text))
    except requests.exceptions.RequestException as e:
        print("Error code: {}".format(e.response.status_code))
