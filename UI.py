# Author Eli Gooding

import tkinter as tk
from os.path import exists
import time


window = tk.Tk()
window.title('zip code entry')
# window.geometry("600X400")
window.geometry("700x200")
usr_input = tk.StringVar()



def ui_inputs():
    location = usr_input.get()
    with open('location.txt', "w") as f:
        f.write(location)
        f.close()


    with open('aqi.txt', 'r') as b:
        aqi = b.read()
    aqi_label.configure(text= "air qualiy index = " + aqi)
    response_exists = exists('response.txt')
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







input_label = tk.Label(window, text = "Location, zip code preferred")
response_label = tk.Label()
response_label.grid(row=0, column=3)
aqi_label = tk.Label()
aqi_label.grid(row=1, column=2)
usr_entry = tk.Entry(window, textvariable=usr_input)

submit_button = tk.Button(window, text = "Submit", command = ui_inputs)

#locations for each item to show
input_label.grid(row=0, column=0)
usr_entry.grid(row=0,column=1)
submit_button.grid(row=0, column=2)

# Terminate button
button2 = tk.Button(window, text='End Now', command=window.destroy)
button2.grid(row=3, column=1)
window.mainloop()
