# Author Eli Gooding
# Description: user interface that requests a zip code from the user to be written in "location.txt" and display the
# sarcastic statement on the temperature then to close the program out when finished


# Imports/Dependencies
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from os.path import exists
import time
import os

# Set up user input window
window = tk.Tk()
window.title('Sarcastic Weather!')
window.geometry("1020x200")
usr_input = tk.StringVar()


def ui_inputs():
    location = usr_input.get()
    with open('location.txt', "w") as f:
        f.write(location)
        f.close()

    # Bools for displaying data to the UI
    response_exists = exists('response.txt')
    aqi_exists = exists('aqi_response.txt')

    # Check for response data from weather_goodnel.py. if not, loop and display when communication arrives.
    if response_exists:
        with open('response.txt', 'r') as sr:
            sarcastic_response = sr.read()
            sr.close()
            response_label.configure(text=sarcastic_response)
    while not response_exists:
        response_exists = exists('response.txt')
        if response_exists:
            with open('response.txt') as sr:
                sarcastic_response = sr.read()
                sr.close()
                response_label.configure(text=sarcastic_response)
        else:
            time.sleep(5)

    # Check for aqui_resonse from AQI. if not, loop and display when communication arrives.
    if aqi_exists:
        with open('aqi_response.txt', 'r') as b:
            aqi = b.read()
        aqi_label.configure(text="air qualiy index states = " + aqi)
    else:
        while not aqi_exists:
            aqi_exists = exists('aqi_response.txt')
            if response_exists:
                with open('aqi_response.txt') as b:
                    aqi = b.read()
                    b.close()
                    aqi_label.configure(text="air qualiy index states = " + aqi)
            else:
                time.sleep(2)


# set up widgets and displays of UI.
input_label = tk.Label(window, text="Enter location.. zip code preferred test others for yourself")
response_label = tk.Label()
response_label.grid(row=0, column=3)
aqi_label = tk.Label()
aqi_label.grid(row=1, column=2)
usr_entry = tk.Entry(window, textvariable=usr_input)

submit_button = tk.Button(window, text="Submit", command=ui_inputs)

# locations for each item to show
input_label.grid(row=0, column=0)
usr_entry.grid(row=0, column=1)
submit_button.grid(row=0, column=2)

# Terminate button
button2 = tk.Button(window, text='End Now', command=window.destroy)
button2.grid(row=3, column=1)
window.mainloop()
