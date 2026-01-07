import requests
from datetime import datetime
from datetime import date, timedelta

def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1}
    response = requests.get(url, params=params).json()
    if "results" in response:
        coords = response["results"][0]
        return coords["latitude"], coords["longitude"]
    return None, None

def fetch_aqi_data(lat, lon):
    end_date = date.today()
    start_date = end_date - timedelta(days=7)

    url = "https://air-quality-api.open-meteo.com/v1/air-quality"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "european_aqi,us_aqi",
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "timezone": "auto"
    }

    response = requests.get(url, params=params)
    return response.json()

def print_last_7_days_aqi(data):
    times = data.get("hourly", {}).get("time", [])
    aqi = data.get("hourly", {}).get("us_aqi", [])
    
    if not times or not aqi:
        print("No AQI data available.")
        return

    # Convert to daily averages
    daily = {}
    for t, q in zip(times, aqi):
        date = t.split("T")[0]
        daily.setdefault(date, []).append(q)

    print(f"\nDate       | Avg AQI")
    print("-" * 24)
    for date in sorted(daily):
        vals = daily[date]
        avg_aqi = sum(vals) / len(vals)
        print(f"{date} | {avg_aqi:.1f}")

def main():
    city = input("Enter city name: ")
    lat, lon = get_coordinates(city)
    if lat is None:
        print("City not found.")
        return

    print(f"Fetching last 7 days’ AQI for {city} ({lat:.4f}, {lon:.4f})...\n")
    data = fetch_aqi_data(lat, lon)
    print_last_7_days_aqi(data)

if __name__ == "__main__":
    main()
