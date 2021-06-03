#!/usr/bin/python3
"""3. Count it"""


def count_words(subreddit, word_list, word_count={}, after=None):
    """prints a sorted count of given keywords"""
    
import requests

    resInf = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if resInf.status_code != 200:
        return None

    inf = resInf.json()

    hotL = [child.get("data").get("title")
             for child in inf
             .get("data")
             .get("children")]
    if not hotL:
        return None

    word_list = list(dict.fromkeys(word_list))

    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for title in hotL:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_count[word] += 1

    if not inf.get("data").get("after"):
        sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
        sorted_counts = sorted(word_count.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, word_count,
                           inf.get("data").get("after"))
