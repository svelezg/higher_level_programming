#!/usr/bin/python3
"""
takes in a string and sends a search request to the Star Wars API
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://swapi.co/api/people"
    values = {'search': sys.argv[1]}
    response = requests.get(url, params=values)
    print("Number of results: {}".format(response.json().get("count")))
    for result in response.json().get("results"):
        print(result.get("name"))
        for film_url in result.get("films"):
            film_response = requests.get(film_url)
            print("\t{}".format(film_response.json().get("title")))

    while response.json().get("next"):
        url = response.json().get("next")
        response = requests.get(url, params=values)
        for result in response.json().get("results"):
            print(result.get("name"))
            for film_url in result.get("films"):
                film_response = requests.get(film_url)
                print("\t{}".format(film_response.json().get("title")))
