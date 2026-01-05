"""
Part 2: Status Codes and JSON Parsing
=====================================
Difficulty: Beginner+

Learn:
- Understanding HTTP status codes
- Parsing JSON data like a Python dictionary
- Accessing specific fields from API response
"""

import requests

print("=== Understanding Status Codes ===\n")

# Example 1: Successful request (200 OK)
print("--- Example 1: Valid Request ---")
url_valid = "https://jsonplaceholder.typicode.com/posts/5"
response = requests.get(url_valid)

print(f"URL: {url_valid}")
print(f"Status Code: {response.status_code}")
print(f"Success? {response.status_code == 200}")                 #checks status code


# Example 2: Not Found (404)
print("\n--- Example 2: Invalid Request (404) ---")
url_invalid = "https://jsonplaceholder.typicode.com/posts/99999"      #invalid
response_404 = requests.get(url_invalid)

print(f"URL: {url_invalid}")
print(f"Status Code: {response_404.status_code}")
print(f"Found? {response_404.status_code == 200}")


# Example 3: Parsing JSON Data
print("\n--- Example 3: Parsing JSON ---")
url = "https://jsonplaceholder.typicode.com/users/1"             #api url for user 1
response = requests.get(url)

# Convert response to Python dictionary
data = response.json()                                           #converts api response to python dictonary

# Access specific fields
print(f"Full Name: {data['name']}")
print(f"Username: {data['username']}")
print(f"Email: {data['email']}")
print(f"City: {data['address']['city']}")
print(f"Company: {data['company']['name']}")


# Example 4: Working with a list of items
print("\n--- Example 4: List of Items ---")
url_list = "https://jsonplaceholder.typicode.com/posts?userId=1"    #url that returns multiple posts for user 1
response = requests.get(url_list)
posts = response.json()

print(f"User 1 has {len(posts)} posts:")
for i, post in enumerate(posts[:3], 1):                              # Show first 3 and enumerate adds numbering
    print(f"  {i}. {post['title'][:40]}...")

# --- COMMON STATUS CODES ---
print("\n--- Common HTTP Status Codes ---")
status_codes = {
    200: "OK - Request successful",
    201: "Created - Resource created",
    400: "Bad Request - Invalid syntax",
    401: "Unauthorized - Authentication required",
    403: "Forbidden - Access denied",
    404: "Not Found - Resource doesn't exist",
    500: "Internal Server Error - Server problem"
}

for code, meaning in status_codes.items():                        #used to print each status code with meaninig\
    print(f"  {code}: {meaning}")


#exercise 1
print("\n--- Exercise 1: User ID 5 Phone number ---")
url = "https://jsonplaceholder.typicode.com/users/5"                 #api url for user id 5

response = requests.get(url)                                         #send get req

if response.status_code == 200:                                      #check req if success
    data = response.json()                                           #convert json to python dict
    print("Phone Number:", data["phone"])
else:
    print("User not found!")


#exercise 2

print("\n--- Exercise 2: Check resource ---")

user_id = input("Enter user ID (1-10): ")                            #user input

if not user_id.isdigit():                                            #input should be numeric only
    print("Invalid input! Please enter a number.")
else:
    user_id = int(user_id)

    if user_id < 1 or user_id > 10:
        print("User ID must be between 1 and 10.")
    else:
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"  #user api
        response = requests.get(url)

        if response.status_code == 200:                                #check if resource exists
            data = response.json()
            print("\nUser Data:")
            print(data)
        else:
            print("Resource not found!")

#exercise 3

print("\n--- Exercise  3: NO. of comments on Post ID 1 ---")

url = "https://jsonplaceholder.typicode.com/posts/1/comments"           #api url to comments of post id 1

response = requests.get(url)

if response.status_code == 200: 
    comments = response.json()
    print("Number of comments on post 1:", len(comments))
else:
    print("Failed to fetch comments!")




# --- EXERCISES ---
#
# Exercise 1: Fetch user with ID 5 and print their phone number                #done
#             URL: https://jsonplaceholder.typicode.com/users/5
#
# Exercise 2: Check if a resource exists before printing data                  #done                  
#             if response.status_code == 200:
#                 print(data)
#             else:
#                 print("Resource not found!")
#
# Exercise 3: Count how many comments are on post ID 1                         #done
#             URL: https://jsonplaceholder.typicode.com/posts/1/comments
