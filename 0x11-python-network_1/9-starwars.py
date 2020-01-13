#!/usr/bin/python3
"""
takes in a string and sends a search request to the Star Wars API
"""
if __name__ == "__main__":
    import requests
    import sys

    url = 'https://swapi.co/api/people'

    if len(sys.argv) != 2:
        search = ""
        print("No result")
    else:
        search = sys.argv[1]
        values = {'search': search}
        response = requests.get(url, params=values)
        print("Number of results: {}".format(response.json().get("count")))
        results = response.json().get("results")
        for result in results:
            print(result.get("name"))
