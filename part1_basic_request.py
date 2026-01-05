"""
Part 1: Basic GET Request
=========================
Difficulty: Beginner

Learn: How to make a simple GET request and view the response.

We'll use JSONPlaceholder - a free fake API for testing.
"""

import requests #accessing library

# Step 1: Define the API URL
url = "https://jsonplaceholder.typicode.com/posts/1"     #this is url used for testing api

# Step 2: Make a GET request
response = requests.get(url)                             #this get request is to get data from that url from step 1

# Step 3: Print the response
print("=== Basic API Request ===\n")                     #prints headining
print(f"URL: {url}")                                     #prints url and f string iis used to put variable inside text
print(f"Status Code: {response.status_code}")            #it tells wether req syccessfull or not
print(f"\nResponse Data:")                               #heading
print(response.json())                                   #prints the data from url response its in json format


# --- EXERCISES ---
# Try these on your own:
#
# Exercise 1: Change the URL to fetch post number 5                  #done
#             Hint: Change /posts/1 to /posts/5
#
# Exercise 2: Fetch a list of all users                              #done
#             URL: https://jsonplaceholder.typicode.com/users
#
# Exercise 3: What happens if you fetch a post that doesn't exist?   #done
#             Try: https://jsonplaceholder.typicode.com/posts/999
