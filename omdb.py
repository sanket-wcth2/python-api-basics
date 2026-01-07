import requests

API_KEY = "9b1a9ef3"
BASE_URL = "http://www.omdbapi.com/"
DEBUG = False   


def fetch_data(params):
    params["apikey"] = API_KEY
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if DEBUG:
        print("DEBUG RESPONSE:", data)

    return data


def search_movie(movie_name):
    if not movie_name.strip():
        print(" Movie name cannot be empty")
        return

    params = {"s": movie_name}
    data = fetch_data(params)

    if data.get("Response") == "True":
        print("\n🎬 Search Results:")
        for i, movie in enumerate(data["Search"], start=1):
            print(f"{i}. {movie['Title']} ({movie['Year']}) | ID: {movie['imdbID']}")
    else:
        print("❌", data.get("Error"))


def movie_details(movie_name):
    if not movie_name.strip():
        print("❌ Movie name cannot be empty")
        return

    params = {
        "t": movie_name,
        "plot": "full"
    }
    movie = fetch_data(params)

    if movie.get("Response") == "True":
        print("\n🎞️ Movie Details")
        print("-" * 40)
        print(f"Title      : {movie['Title']}")
        print(f"Year       : {movie['Year']}")
        print(f"Genre      : {movie['Genre']}")
        print(f"Runtime   : {movie['Runtime']}")
        print(f"Director  : {movie['Director']}")
        print(f"Actors    : {movie['Actors']}")
        print(f"IMDb      : {movie['imdbRating']}")
        print(f"BoxOffice : {movie.get('BoxOffice', 'N/A')}")
        print(f"Awards    : {movie['Awards']}")

        print("\n⭐ Ratings:")
        for rating in movie.get("Ratings", []):
            print(f"- {rating['Source']}: {rating['Value']}")

        print("\nPlot:")
        print(movie["Plot"])
    else:
        print("❌", movie.get("Error"))


def main():
    while True:
        print("\n🎥 Welcome to Movie Explorer 🎥")
        print("1. Search Movie")
        print("2. Movie Details")
        print("3. Exit")

        choice = input("Choose an option : ")

        if choice == "1":
            name = input("Enter movie name: ")
            search_movie(name)
        elif choice == "2":
            name = input("Enter exact movie name: ")
            movie_details(name)
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    main()
