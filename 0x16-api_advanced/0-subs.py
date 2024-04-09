#!/usr/bin/python3
"""Module for task 0"""


import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        subscribers = data.get("subscribers")
        return subscribers
    else:
        print("Error: Status code", response.status_code)
        print("Response:", response.content)
        return 0

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
        sys.exit(1)

    subreddit = sys.argv[1]
    subscribers = number_of_subscribers(subreddit)
    print(subscribers)
