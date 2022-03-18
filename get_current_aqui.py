#
# OSU CS361: Intro to Software Development 1
# Air Quality Index Microservice
# Winter 2022
#
# Author: Maggie Liu
# Version: 2.0.0
# Description: A microservice to return current air quality information from a supplied location string.
#

from geopy import geocoders
import requests
from os.path import exists
import time


# Get location request from a text file
# Can be a city, postal code, or combination

location_exists = exists('location.txt')
while not location_exists:
    location_exists = exists('location.txt')
    print(location_exists)
    if location_exists:
        with open('location.txt', 'r') as infile:
            location = infile.readline()
        # Covert supplied location to lat/long
        locator = geocoders.Nominatim(user_agent="aqi_microservice")
        city = locator.geocode(location)
        latitude = city.latitude
        longitude = city.longitude
    time.sleep(2)

    # Get AQI data from Open Weather Map
open_weather_map_key = "9874f807c9c65eed1d03fcf8fc332a6f"
url = "http://api.openweathermap.org/data/2.5/air_pollution?lat=" + str(latitude) + "&lon=" + str(longitude) + "&appid=" + open_weather_map_key
data = requests.get(url).json()

# Isolate the AQI from the returned information. Open Weather Map uses a 1 - 5 scale.
aqi_data = str(data['list'][0]['main']['aqi'])

# Write data to the input file
with open('current_aqi.txt', 'w') as outfile:
    outfile.write(aqi_data)

print(aqi_data)