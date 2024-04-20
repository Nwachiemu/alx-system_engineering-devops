#!/usr/bin/python3
"""Recursive function which verifies the Reddit API"""
import re
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """Recursively counts occurrences of specific words"""

    if word_count is None:
        word_count = {}

    if after is None:
        after = ""

    url = 'https://www.reddit.com/r/{}/hot/.json'
    user = {"User-Agent": "Linux Nwachi"}
    params = {"after": after, "limit": 100}

    try:
        r = requests.get(url.format(subreddit),
                         headers=user,
                         params=params,
                         allow_redirects=False)

        if r.status_code != 200:
            return

        data = r.json().get("data", {})
        after = data.get("after", "")
        children = data.get("children", [])
        conc = " ".join(post["data"]["title"] for post in children)
        ls_lower = [word.lower() for word in word_list]

        for w in ls_lower:
            count = len(re.findall(r'\b{}\b'.format(re.escape(w)),
                                   conc.lower()))
            if count > 0:
                if w in word_count:
                    word_count[w] += count
                else:
                    word_count[w] = count

        if after:
            count_words(subreddit, word_list, after, word_count)
        else:
            sorted_words = sorted(word_count.items(),
                                  key=lambda x: (-x[1], x[0]))
            return sorted_words

    except Exception:
        pass
