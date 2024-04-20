#!/usr/bin/python3
"""Function which addresses Reddit API"""


import requests


def top_ten(subreddit):
    """Returns ls of titles of the first ten hot posts"""
    url = 'https://www.reddit.com/r/{}/hot.json'
    usr = {'User-Agent': 'Linux Nwachi'}
    heads = []

    try:
        r = requests.get(url.format(subreddit),
                                headers=usr, params={'limit': 10},
                                allow_redirects=False)

        if r.status_code == 200:
            info = r.json()
            posts = info['data']['children']
            for post in posts:
                t = post['data']['title']
                heads.append(t)
        else:
            return None

    except Exception:
        return None

    return heads
