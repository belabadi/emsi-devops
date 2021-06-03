#!/usr/bin/python3
"""2. Recurse it"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """returns a list containing the titles of all hot articles for a given subreddit"""

    import requests

    resInf = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if resInf.status_code >= 400:
        return None

    hotL = hot_list + [child.get("data").get("title")
                        for child in resInf.json()
                        .get("data")
                        .get("children")]

    inf = resInf.json()
    if not inf.get("data").get("after"):
        return hotL

    return recurse(subreddit, hotL, inf.get("data").get("count"),
                   inf.get("data").get("after"))
