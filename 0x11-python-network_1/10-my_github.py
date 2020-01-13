#!/usr/bin/python3
"""
takes your Github credentials (username and password) and
uses the Github API to display your id
"""
if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/user"

    if len(sys.argv) != 3:
        username = ""
        password = ""
        print("No result")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        response = requests.get(url, auth=(username, password))
        print(response.json().get("id"))
