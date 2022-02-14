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
    # print("this is the type:" , type(weather.current.temperature))

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()


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
