#
# Author: Eli Gooding
# Description: this file looks for a txt file called "location.txt" containing a zip code to then use web api
# python_weather to get the temperature, send it to statement function to return a sarcastic statement on the weather
# in a file called "response.txt"


import python_weather
import asyncio
from os.path import exists
import time


async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # look for incoming files to exist which tells the microservice to run and look for location or air quality
    location_exists = False
    print(location_exists)
    aqi_exists = False

    # wait until location has been communicated from user input.
    while not location_exists:
        location_exists = exists('location.txt')
        print(location_exists)
        if location_exists:
            # read incoming weather location request
            with open('location.txt', 'r') as file:
                usr_input = str(file.read())
                file.close()
        time.sleep(2)

    print(usr_input)

    # fetch a weather forecast from the city user defines
    weather = await client.find(str(usr_input))

    # print in console so that someone debugging can review
    print(f"Your location of interest is: " + weather.location_name)
    print(f"your sky looks like" + weather.current.sky_text)

    with open('weather.txt', 'w') as f:
        f.write(str(weather.current.temperature))

    # If teammates microservice isn't present, then wait until present. Then read aqi number.
    while not aqi_exists:
        aqi_exists = exists('current_aqi.txt')
        if aqi_exists:
            with open('current_aqi.txt', 'r') as b:
                aqi = b.read()
                b.close()
            aqiStatement(int(aqi))
            with open('aqi_response.txt', 'w') as f:
                f.write(aqiStatement(int(aqi)))
                f.close()
        time.sleep(2)

    print("you air quality index = ", aqi)
    # returns the current day's forecast temperature (int)
    print("your current weather = ", weather.current.temperature)
    print(statement(weather.current.temperature))

    with open('response.txt', 'w') as r:
        r.write(str(weather.current.temperature) + " degrees... " + statement(weather.current.temperature))
    await client.close()


# Statement
def statement(temp):
    above80 = "Better know how to make a swamp air conditioner"
    between79and70 = "Grab a beer 'cause its a little hot"
    between50and69 = "Perfection... sunglasses and chill"
    between49and32 = "Chilly but all is good. Nothing a beer cant handle."
    between31and20 = "COLD"
    between19and10 = "Really COLD"
    between9and0 = "Yeah Really Really COLD"
    belowzero = "Stay home... alcohol is friend"

    if temp > 80:
        return above80
    elif temp < 80 and temp >= 70:
        return between79and70
    elif temp < 70 and temp >= 50:
        return between50and69
    elif temp < 50 and temp >= 32:
        return between49and32
    elif temp < 32 and temp >= 20:
        return between31and20
    elif temp < 20 and temp >= 10:
        return between19and10
    elif temp < 10 and temp >= 0:
        return between9and0
    else:
        return belowzero


def aqiStatement(aqi):
    aboveFive = "Hazardous"
    five = "Very Unhealthy"
    four = "Unhealthy"
    three = "Unhealthy for Sensitive Groups"
    two = "Moderate"
    one = "Good"
    category = ""

    if aqi > 5:
        return aboveFive
    elif aqi == 5:
        return five
    elif aqi == 4:
        return four
    elif aqi == 3:
        return three
    elif aqi == 2:
        return two
    elif aqi == 1:
        return one


# usr_input= input("city of interest? please enter here")
# getweather(usr_input)


# usr_input = input("input your city and state of interest: ")
# Initialize GUI for user to enter city state or zip
# usr_input = tk.StringVar()
# closebutton = tk.Button(window, text='End Now', width=50, command=window.destroy)
# closebutton.pack(fill='x', expand=True)
# field_entry = tk.Entry(window,textvariable=usr_input)
# field_entry.pack(fill='x', expand=True)
# button = tk.Button(window, text='Submit', width=50, command=getweather)
# button.pack(fill='x', expand=True)
loop = asyncio.get_event_loop()
loop.run_until_complete(getweather())
# window.mainloop()
