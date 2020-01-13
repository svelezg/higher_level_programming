#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) != 2:
        q = ""
        print("No result")
    else:
        q = sys.argv[1]
        values = {'q': q}
        response = requests.post(url, data=values)
        try:
            output = response.json()
            if output:
                print("[{}] {}".format(output.get("id"), output.get("name")))
            else:
                print("No result")
        except Exception:
            print("Not a valid JSON")
