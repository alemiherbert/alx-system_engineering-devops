#!/usr/bin/python3

""""This module contains a function that queries a given subreddit"""
import requests

def number_of_subscribers(subreddit):
    """This function queries a given subreddit and
    returns the number of subscribers"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Google Chrome 80"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
