#!/usr/bin/python3
'''A module for interacting with the Reddit API to count word occurrences.
'''
import requests


def print_sorted_histogram(histogram):
    '''Sorts and prints the histogram in descending order of word frequency.
    '''
    filtered_histogram = {k: v for k, v in histogram.items() if v > 0}
    sorted_histogram = sorted(
        filtered_histogram.items(),
        key=lambda kv: (-kv[1], kv[0])
    )
    for word, count in sorted_histogram:
        print(f'{word}: {count}')


def count_words(subreddit, word_list, histogram=None, count=0, after=None):
    '''Counts occurrences of each word in the given word list within a subreddit's titles.
    '''
    if histogram is None:
        word_list = [word.lower() for word in word_list]
        histogram = {word: 0 for word in word_list}

    headers = {
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.71 Safari/537.36 '
                      'Edg/97.0.1072.62'
    }

    params = {
        'sort': 'hot',
        'limit': 30,
        'count': count,
        'after': after
    }

    url = f'https://www.reddit.com/r/{subreddit}/.json'
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        posts = data.get('children', [])
        titles = [post['data']['title'].lower() for post in posts]

        for title in titles:
            words = title.split()
            for word in word_list:
                histogram[word] += words.count(word)

        if len(posts) == params['limit'] and data.get('after'):
            count_words(subreddit, word_list, histogram,
                        count + len(posts), data['after'])
        else:
            print_sorted_histogram(histogram)
    else:
        return
