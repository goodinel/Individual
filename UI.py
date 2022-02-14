# Author Eli Gooding

import tkinter as tk

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
    print(usr_input)


input_label = tk.Label(window, text = "Location, zip code preferred")
usr_entry = tk.Entry(window, textvariable = usr_input)

submit_button = tk.Button(window, text = "Submit", command = ui_inputs)

#locations for each item to show
input_label.grid(row=0, column=0)
usr_entry.grid(row=0,column=1)
submit_button.grid(row=0, column=2)

# Terminate button
button2 = tk.Button(window, text='End Now', command=window.destroy)
button2.grid(row=2, column=1)
window.mainloop()
