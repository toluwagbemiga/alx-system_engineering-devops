#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{subreddit}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")


if __name__ == "__main__":
    import sys

    subreddit = sys.argv[1] if len(sys.argv) > 1 else None
    if not subreddit:
        print("Usage: python3 0-main.py <subreddit>")
        sys.exit(1)

    subscribers = number_of_subscribers(subreddit)
    print("{}: {}".format(subreddit, subscribers))
