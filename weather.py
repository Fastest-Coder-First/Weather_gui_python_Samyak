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
root.attributes('-fullscreen', True)
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
        humidity = weather_data['main']["humidity"]
        pressure = weather_data['main']["pressure"]

        # Update weather details labels
        temperature_label.config(text=" {:.1f} °C".format(temperature))
        description_label.config(text="Description: {}".format(description))
        wind_speed_label.config(text="Wind Speed: {} m/s".format(wind_speed))
        humidity_label.config(text="Humidity: {}%".format(humidity))
        pressure_label.config(text="Pressure: {} hPa".format(pressure))
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
description_label = Label(weather_frame, text="Description:", font=('Arial', 16))
description_label.pack(pady=10)
wind_speed_label = Label(weather_frame, text="Wind Speed:", font=('Arial', 16))
wind_speed_label.pack(pady=10)
humidity_label = Label(weather_frame, text="Humidity:", font=('Arial', 16))
humidity_label.pack(pady=10)
pressure_label = Label(weather_frame, text="Pressure:", font=('Arial', 16))
pressure_label.pack(pady=10)

# Temperature label should appear at the top of the GUI, centered and with larger text and bold
temperature_label = Label(root, text="", font=('Arial', 30, 'bold'))
temperature_label.place(relx=0.5, y=50, anchor=CENTER)
temperature_label.configure(background=root.cget('background'))

#a exit button
def exit_app(event=None):
    root.destroy()

exit_button = Button(root, text='Exit', command=exit_app, bg='red', fg='white', font=('Arial', 14))
exit_button.place(x=10, y=10)

# Bind the <Escape> key event to exit_app function
root.bind("<Escape>", exit_app)



root.mainloop()



# %%
