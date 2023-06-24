#%%
#weather gui make it look like a web app , its gui should be similar to ios add background image , transparent divs inside gui in which we can forecast history of weather in a particular city

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import requests
from PIL import ImageTk, Image
from io import BytesIO

root = Tk()
root.title("Weather App")
root.geometry("600x400")

# Set background image
background_image = Image.open("bg.jpeg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Weather Details Frame
weather_frame = Frame(root, bg="white", bd=5)
weather_frame.place(relx=0.5, rely=0.5, anchor=CENTER)



# Function to retrieve weather data
def get_weather():
    api_key = "b3ff5fa6f2e4642a02a0d87e4caee434"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city.get()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    weather_data = response.json()

    if weather_data["cod"] != "404":
        temperature = weather_data['main']["temp"] - 273.15
        description = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]

        # Update weather details labels
        temperature_label.config(text="Temperature: {:.1f} °C".format(temperature))
        description_label.config(text="Description: {}".format(description))
        wind_speed_label.config(text="Wind Speed: {} m/s".format(wind_speed))
    else:
        messagebox.showerror("Error", "City Not Found")

# City Entry
city = StringVar()
city_entry = Entry(weather_frame, textvariable=city, font=('Arial', 14))
city_entry.pack(pady=20)
city_entry.focus_set()

# Search Button
search_button = Button(weather_frame, text='Search', command=get_weather, bg='blue', fg='white', font=('Arial', 14))
search_button.pack()

# Weather Details Labels
temperature_label = Label(weather_frame, text="Temperature:", font=('Arial', 16))
temperature_label.pack(pady=10)
description_label = Label(weather_frame, text="Description:", font=('Arial', 16))
description_label.pack(pady=10)
wind_speed_label = Label(weather_frame, text="Wind Speed:", font=('Arial', 16))
wind_speed_label.pack(pady=10)

root.mainloop()

       
        



        











# %%
