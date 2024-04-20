#!/usr/bin/python3
"""Function which addresses Reddit API"""


import requests


def number_of_subscribers(subreddit):
    """Gets number of subscribers on a subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'
    user = {'User-Agent': 'Linux Nwachi'}

    try:
        r = requests.get(url.format(subreddit),
                         headers=user,
                         allow_redirects=False)
        info = r.json()
        subs = info['data']['subscribers']
        return subs
    except Exception:
        return 0
