#!/usr/bin/python3
"""Recursive function that queries the Reddit API"""


import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a subreddit"""
    url = 'https://www.reddit.com/r/{}/hot/.json'
    usr = {'User-Agent': 'Linux David'}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        r = requests.get(url.format(subreddit),
                                headers=usr,
                                params=params,
                                allow_redirects=False)
        if r.status_code == 404:
            return None

        results = r.json().get("data")
        after = results.get("after")
        count += results.get("dist")

        for c in results.get("children"):
            hot_list.append(c.get("data").get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after, count)

        return hot_list

    except Exception:
        return None
    