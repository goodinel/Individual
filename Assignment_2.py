import tkinter as tk
import time
# from PIL import ImageTk, Image

# define run start function for writing 'run' into prng-service.txt
def ui_run_start():
    # with open('location.txt.txt', 'w') as file:
    #     file.close()

    # Show the randomly generated number
    # Initialize While Bool
    start_stop = True
    while start_stop:
        with open('prng-service.txt', 'r+') as file:
            line = file.readline()
            if line != 'run':
                rand_num = line
                file.close()
                start_stop = False
            else:
                time.sleep(2)
                file.close()

    path = "C:\\Users\\votef\\PycharmProjects\\CS361\\CS361_Project\\bee_imgs\\" + rand_num + ".png"
    # Show random number and file path
    prng_result.configure(text="Random number: " + rand_num)
    img_res.configure(text="File Path:" + path)
    return


# Define window and minimal css
window = tk.Tk()
window.title('Assignment 2')
window.geometry("700x200")
# window.configure(bg='#856ff8')

# Initialize random image generator.
# image_service_button = tk.Button(window, text="Image Service", width=30, command=image_service)
# image_service_button.grid(row=1, column=0)
canvas = tk.Canvas(window, width=300, height=300)
canvas.grid(row=3, column=2)
img_res = tk.Label()
img_res.grid(row=1, column=1)


# random number generation buttons and fields
button = tk.Button(window, text='Run Me First (PRNG)', width=30, command=ui_run_start)
button.grid(row=0, column=0)
prng_result = tk.Label()
prng_result.grid(row=0, column=1)

# Destroy and end program
button2 = tk.Button(window, text='End Now', width=50, command=window.destroy)
button2.grid(row=2, column=1)
window.mainloop()