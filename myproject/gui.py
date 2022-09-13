import webbrowser
from tkinter import *
from tkinter import ttk
from isslocation import iss_lat, iss_long
import sv_ttk


# When the update button is clicked, the iss_lat and iss_long functions are called and the values are displayed in the labels
def update_location():
    lat = iss_lat()
    long = iss_long()
    lat_label.config(text=lat)
    long_label.config(text=long)

# Place the coordinates in google maps
def google_maps():
    lat = iss_lat()
    long = iss_long()
    webbrowser.open("https://www.google.com/maps/place/" + lat + "," + long)




# The window
window = Tk()
sv_ttk.set_theme("dark")
window.title("ISS Location")
window.geometry("300x300")

#Add icon to window


# Add message greeting the user
greeting = Label(text="Welcome to the ISS Location App.")

#Exit button
exit_button = ttk.Button(text="Exit", command=window.destroy, width=10)

# Lat and Long Text
lat_text = Label(text="Latitude:")
long_text = Label(text="Longitude:")




# Create the labels
lat_label = Label(window, text="Latitude")
long_label = Label(window, text="Longitude")

#Show image in google maps button
google_maps_button = ttk.Button(text="Show in Google Maps", command=google_maps)

# Create the update button
update_button = ttk.Button(window, text="Update",  command=update_location,)

# The layout
# Latitute and Longitude labels below the greeting

greeting.grid(row=0, column=0, columnspan=2)

# Adding the exit button beside the update button
exit_button.grid(row=4, column=1)
lat_label.grid(row=1, column=2)
long_label.grid(row=2, column=2)

#Add the google maps button
google_maps_button.grid(row=5, column=1, columnspan=2)


# The latitude and longitude text labels beside the latitude and longitude labels
lat_text.grid(row=1, column=1)
long_text.grid(row=2, column=1)

#place update button in the bottom right corner
update_button.grid(row=3, column=1, columnspan=2)
greeting.grid(row=0, column=0, sticky="w")

# Run the main window loop
window.mainloop()
   


