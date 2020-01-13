#!/usr/bin/python3
"""
takes in a string and sends a search request to the Star Wars API
"""
if __name__ == "__main__":
    import requests
    import sys

    url = 'https://swapi.co/api/people'

    search = sys.argv[1]
    values = {'search': search}

    response = requests.get(url, params=values)
    print("Number of results: {}".format(response.json().get("count")))
    results = response.json().get("results")
    for result in results:
        print(result.get("name"))
        films_url = result.get("films")
        for film_url in films_url:

            film_response = requests.get(film_url)
            film_results = film_response.json().get("title")
            print("\t{}".format(film_results))

    while 1:
        if response.json().get("next") is None:
            break
        url = response.json().get("next")
        response = requests.get(url, params=values)
        results = response.json().get("results")
        for result in results:
            print(result.get("name"))
            films_url = result.get("films")
            for film_url in films_url:
                film_response = requests.get(film_url)
                film_results = film_response.json().get("title")
                print("\t{}".format(film_results))
