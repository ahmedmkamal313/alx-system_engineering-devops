#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of
subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    # URL for the Reddit API endpoint to get subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'my-app/0.0.1'}

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and return the number of subscribers
        data = response.json()
        return data['data']['subscribers']
    else:
        # Return 0 for invalid subreddits or other errors
        return 0


if __name__ == "__main__":
    # Example usage from the command line
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
