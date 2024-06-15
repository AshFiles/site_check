"""
This script checks whether a specified website is up and measures the time it takes to load the page.

How to run:
Run the script with the URL as an argument:
   python check_site.py http://ashwinik.com
"""

import requests
import time
import argparse
import sys

def check_site_status(url):
    try:
        # Record the start time before making the request
        start_time = time.time()
        # Make an HTTP GET request to the specified URL
        response = requests.get(url)
        # Record the end time after the request completes
        end_time = time.time()
        
        # Calculate the load time
        load_time = end_time - start_time

        # Check if the status code is 200
        if response.status_code == 200:
            print(f"The site {url} is up. It took {load_time:.2f} seconds to load the page.")
            sys.exit(0)  # Exit with code 0 (success)
        else:
            print(f"The site {url} is down or not reachable. Status code: {response.status_code}")
            sys.exit(1)  # Exit with code 1 (failure)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)  # Exit with code 1 (failure)

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Check if a site is up and measure load time.")
    parser.add_argument("url", help="The URL of the site to check")
    
    # Parse the arguments
    args = parser.parse_args()
    # Check the site status
    check_site_status(args.url)