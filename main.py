import python_weather
import asyncio

async def getweather(usr_input):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find(usr_input)
    print(f"Your location of interest is: " + weather.location_name)

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)
    # print("this is the type:" , type(weather.current.temperature))

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    usr_input = input("input your city and state of interest: ")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather(usr_input))
