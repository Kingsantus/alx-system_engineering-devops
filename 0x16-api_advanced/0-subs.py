#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests

def number_of_subscribers(subreddit):
    """Request number of subscribers of subreddit
    from Reddit API
    """
    # Set custom user-agent
    user_agent = '0x16-api_advanced-kingsantus'
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Custom user-agent avoids request limit
    headers = {'User-Agent': user_agent}

    try:
        r = requests.get(url, headers=headers, allow_redirects=False)
        r.raise_for_status()  # Raise an exception for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        # Handle exceptions, for example, if there's a network error
        print(f"Error: {e}")
        return 0

    if r.status_code == 200:
        # Parse the JSON response
        data = r.json()

        # Extract and return the number of subscribers
        return data['data']['subscribers']
    else:
        return 0
