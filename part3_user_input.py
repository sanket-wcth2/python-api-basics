"""
Part 3: Dynamic Queries with User Input
=======================================
Difficulty: Intermediate

Learn:
- Using input() to make dynamic API requests
- Building URLs with f-strings
- Query parameters in URLs
"""

import requests


def get_user_info():                                                             #func to fetch user details from api
    """Fetch user info based on user input."""
    print("=== User Information Lookup ===\n")

    user_id = input("Enter user ID (1-10): ")                                    # take input 
    if not user_id.isdigit():
        print("Invalid input! Please enter a number.")
        return

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"                #to get info from api 
    response = requests.get(url)                                                 #get req to api

    if response.status_code == 200:
        data = response.json()                                                   #convert api response to python dict
        print(f"\n--- User #{user_id} Info ---")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Website: {data['website']}")
    else:
        print(f"\nUser with ID {user_id} not found!")


def search_posts():                                                              #func to fetch user posts
    """Search posts by user ID."""
    print("\n=== Post Search ===\n")

    user_id = input("Enter user ID to see their posts (1-10): ")                 #fetching posts based on user id
    if not user_id.isdigit():
        print("Invalid input! Please enter a numeric user ID.")
        return

    url = "https://jsonplaceholder.typicode.com/posts"                           #url to posts 
    params = {"userId": user_id}

    response = requests.get(url, params=params)
    posts = response.json()

    if posts:
        print(f"\n--- Posts by User #{user_id} ---")
        for i, post in enumerate(posts, 1):                                       #enumerate used to add numbering
            print(f"{i}. {post['title']}")                                        #no and title
    else:
        print("No posts found for this user.")


def get_crypto_price():                                                           #func to get crypto price
    """Fetch cryptocurrency price based on user input."""
    print("\n=== Cryptocurrency Price Checker ===\n")

    print("Available coins: btc-bitcoin, eth-ethereum, doge-dogecoin")            #available options to check
    coin_id = input("Enter coin ID (e.g., btc-bitcoin): ").lower().strip()

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"                     #cypto api url
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price_usd = data['quotes']['USD']['price']                                #price
        change_24h = data['quotes']['USD']['percent_change_24h']                  #24 hr percent price change

        print(f"\n--- {data['name']} ({data['symbol']}) ---")
        print(f"Price: ${price_usd:,.2f}")
        print(f"24h Change: {change_24h:+.2f}%")                                  #prinyts 24 hr change
    else:
        print(f"\nCoin '{coin_id}' not found!")
        print("Try: btc-bitcoin, eth-ethereum, doge-dogecoin")


def get_post_comments():                                                          #func to get comments on posts
    """Print comments for a given post."""
    print("\n=== Post Comments ===\n")

    post_id = input("Enter post ID (1-100): ")
    if not post_id.isdigit():
        print("Invalid input! Post ID must be a number.")
        return

    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"        #api comments
    response = requests.get(url)
    comments = response.json()

    if comments:
        print(f"\n--- Comments for Post #{post_id} ---")
        for i, comment in enumerate(comments, 1):
            print(f"\n{i}. {comment['name']}")
            print(f"   Email: {comment['email']}")
            print(f"   Comment: {comment['body']}")
    else:
        print("No comments found for this post.")


def get_user_todos():                                                             #func for user todos
    """Print TODOs for a user."""
    print("\n=== User TODOs ===\n")

    user_id = input("Enter user ID (1-10): ")
    if not user_id.isdigit():
        print("Invalid input! User ID must be numeric.")
        return

    url = "https://jsonplaceholder.typicode.com/todos"                            #url totdo api
    params = {"userId": user_id}

    response = requests.get(url, params=params)
    todos = response.json()

    if todos:
        print(f"\n--- TODOs for User #{user_id} ---")
        for i, todo in enumerate(todos, 1):
            status = "Completed = True" if todo['completed'] else "Not Completed = False"
            print(f"{i}. {todo['title']} - {status}")
    else:
        print("No TODOs found for this user.")

#exercise 1

CITIES = {
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "chennai": (13.0827, 80.2707),
    "kolkata": (22.5726, 88.3639),
    "hyderabad": (17.3850, 78.4867),
    "pune": (18.5204, 73.8567),
    "ahmedabad": (23.0225, 72.5714),
    "jaipur": (26.9124, 75.7873),
    "nashik": (19.9974, 73.7898),     
    "new york": (40.7128, -74.0060),
    "london": (51.5074, -0.1278),
    "tokyo": (35.6762, 139.6503),
    "sydney": (-33.8688, 151.2093),
    "seoul": (37.5665, 126.9780),
    "singapore": (1.3521, 103.8198),
    "dubai": (25.2048, 55.2708),
}

def get_weather():  
    """Fetch weather for a city using Open-Meteo API."""
    print("\n=== Weather Lookup ===")
    print("Available cities:", ", ".join(CITIES.keys()))

    city = input("Enter city name: ").lower().strip()

    if city not in CITIES:
        print("City not found!")
        return

    latitude, longitude = CITIES[city]

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        current = data["current_weather"]

        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {current['temperature']}°C")
        print(f"Wind Speed: {current['windspeed']} km/h")
        print(f"Wind Direction: {current['winddirection']}°")
    else:
        print("Failed to fetch weather data.")



def main():                                                                          #main 
    """Main menu for the program."""
    print("=" * 40)
    print("  Dynamic API Query Demo")
    print("=" * 40)

    while True:                                                                     #infinte loop
        print("\nChoose an option:")
        print("1. Look up user info")
        print("2. Search posts by user")
        print("3. Check crypto price")
        print("4. View comments for a post")
        print("5. View user TODOs")
        print("6. Get weather by city name")
        print("7. Exit")

        choice = input("\nEnter choice (1-7): ")                                    #choices

        if choice == "1":
            get_user_info()
        elif choice == "2":
            search_posts()
        elif choice == "3":
            get_crypto_price()
        elif choice == "4":
            get_post_comments()
        elif choice == "5":
            get_user_todos()
        elif choice == "6":
            get_weather()   
        elif choice == "7":
            print("\nGoodbye!")
            break                                                                   #after entering choice 6 loop breaks
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()                                                                        #starts


# --- EXERCISES ---
#
# Exercise 1: Add a function to fetch weather for a city
#             Use Open-Meteo API (no key required):
#             https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true
#             Challenge: Let user input city name (you'll need to find lat/long)
#
# Exercise 2: Add a function to search todos by completion status                                                 #done
#             URL: https://jsonplaceholder.typicode.com/todos
#             Params: completed=true or completed=false
#
# Exercise 3: Add input validation (check if user_id is a number)                                                 #done
