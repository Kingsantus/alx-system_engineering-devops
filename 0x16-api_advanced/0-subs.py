#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        'User-Agent': "MyRedditBot/1.0"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Step 4: Check Response Status
        if response.status_code != 200:
            return 0

        # Step 5: Parse JSON Response
        data = response.json()
        subscribers = data['data']['subscribers']

        # Step 9: Return Number of Subscribers
        return subscribers
    except Exception as e:
        # Step 8: Handle Invalid Subreddit
        print(f"An error occurred: {e}")
        return 0
