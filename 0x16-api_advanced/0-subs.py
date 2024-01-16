#!/usr/bin/python3
"""Query Reddit API to determine subreddit sub count
"""

import requests

def number_of_subscribers(subreddit):
    """Request number of subscribers of subreddit
    from Reddit API
    """
    # Set custom user-agent
    user_agent = '0x16-api_advanced-jmajetich'
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Custom user-agent avoids request limit
    headers = {'User-Agent': user_agent}

    # Use allow_redirects=False to avoid following redirects
    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code != 200:
        return 0

    # Load response unit from JSON
    data = r.json()['data']
    # Extract list of pages
    pages = data['children']
    # Extract data from the first page
    page_data = pages[0]['data']
    # Return the number of subreddit subs
    return page_data['subreddit_subscribers']
