#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""
if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/repos/{}/{}/commits".\
        format(sys.argv[2], sys.argv[1])
    param = {"per_page": "10"}
    response = requests.get(url, params=param)

    for result in response.json():
        print("{}: {}".format(result['sha'],
                              result['commit']['author']['name']))
