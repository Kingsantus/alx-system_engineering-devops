#!/usr/bin/python3
#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests

def top_ten(subreddit):
    """
    Prints the top 10 hot posts in a subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    headers = {
        'User-Agent' : "ALX"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    except Exception as e:
        print(None)
