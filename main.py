import python_weather
import asyncio
import tkinter as tk

# window = tk.Tk()
# window.title('Sarcastic Weather')
# window.geometry("700x200")


async def getweather(usr_input):
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find(usr_input)
    print(f"Your location of interest is: " + weather.location_name)

    with open('weather.txt', 'w') as f:
        f.write(str(weather.current.temperature))

    with open('aqi.txt', 'w') as a:
        a.write(str(23))

    with open('aqi.txt', 'r') as b:
        aqi = b.read()

    print("you air quality index = ",aqi)
    # returns the current day's forecast temperature (int)
    print("your current weather = ", weather.current.temperature)
    print(statement(weather.current.temperature))
    # print("this is the type:" , type(weather.current.temperature))

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()


def statement(temp):
    above80 = "Better know how to make a swamp air conditioner"
    between79and70 = "Grab a beer 'cause its a little hot"
    between50and69 = "Perfection... sunglasses and chill"
    between49and32 = "Chilly but all is good"
    between31and20 = "COLD"
    between19and10 = "Really COLD"
    between9and0   = "Yeah Really Really COLD"
    belowzero      = "Stay home... alcohol is friend"

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


usr_input= input("city of interest? please enter here")
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
loop.run_until_complete(getweather(usr_input))
# window.mainloop()
