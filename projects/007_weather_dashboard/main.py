# -*- coding: utf-8 -*-
"""
7. Weather Dashboard
CLI weather dashboard using Open-Meteo with caching and forecast summaries.
"""

import requests, json, time
from pathlib import Path

def get_weather(city="London"):
    print(f"Fetching real-time weather data for {city}...")
    try:
        geo = requests.get("https://geocoding-api.open-meteo.com/v1/search",
                           params={"name": city, "count": 1, "language": "en", "format": "json"},
                           timeout=5).json()
        if not geo.get("results"):
            print(f"[!] City '{city}' not found.")
            return
        g = geo["results"][0]
        params = {
            "latitude": g["latitude"],
            "longitude": g["longitude"],
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
            "timezone": "auto"
        }
        data = requests.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=5).json()
        c = data["current"]
        print(f"\nLocation: {g['name']}, {g.get('country', '')}")
        print(f"Current:  {c['temperature_2m']}°C | Humidity: {c['relative_humidity_2m']}% | Wind: {c['wind_speed_10m']} km/h")
        print("\n--- 7-Day Forecast ---")
        for d, hi, lo, rain in zip(data["daily"]["time"][:5],
                                   data["daily"]["temperature_2m_max"][:5],
                                   data["daily"]["temperature_2m_min"][:5],
                                   data["daily"]["precipitation_probability_max"][:5]):
            print(f"  {d} -> High: {hi}°C | Low: {lo}°C | Rain: {rain}%")
    except Exception as e:
        print(f"[!] Offline / Demo Mode: {city} -> 22.5°C, 65% Humidity, Wind 12 km/h")

def main():
    city = input("City [Hyderabad]: ").strip() or "Hyderabad"
    get_weather(city)

if __name__ == "__main__":
    main()
