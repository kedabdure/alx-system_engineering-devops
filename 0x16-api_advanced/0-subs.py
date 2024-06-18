#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Queries the Reddit API and returns the number of subscribers for a given subreddit. """
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; MyRedditApp/1.0; +https://www.example.com/my-reddit-app)'
    }

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return 0

    data = response.json().get('data', {})
    return data.get('subscribers', 0)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
