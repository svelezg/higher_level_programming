#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.error
    from sys import argv

    url = argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            response = response.read()
            print("{}".format(response.decode('utf-8')))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
