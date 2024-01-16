#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "YourUniqueUserAgent/1.0 by /u/YourRedditUsername"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Parse the JSON response and return the number of subscribers
        results = response.json().get("data")
        return results.get("subscribers")

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (e.g., 403 Forbidden)
        print(f"HTTP error occurred: {http_err}")
        return 0

    except requests.exceptions.RequestException as req_err:
        # Handle other request errors
        print(f"Request error occurred: {req_err}")
        return 0

    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
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

