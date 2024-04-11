import requests

def recurse(subreddit, hot_list=[], after=None, count=0, max_posts=None):
    """
    Recursively retrieves a list of titles of all hot posts
    on a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store the post titles.
                                    Default is an empty list.
        after (str, optional): Token used for pagination.
                                Default is None.
        count (int, optional): Current count of retrieved posts. Default is 0.
        max_posts (int, optional): Maximum number of posts to retrieve. Default is None.
    Returns:
        list: A list of post titles from the hot section of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "My-Reddit-Scraper/1.0"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))
        if max_posts and len(hot_list) >= max_posts:
            return hot_list

    if after is not None:
        return recurse(subreddit, hot_list, after, count, max_posts)

    return hot_list