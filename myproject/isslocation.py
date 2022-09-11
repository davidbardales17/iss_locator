from urllib import response
from webbrowser import get
import requests





#function to return the iss_lat

def iss_lat():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response = response.json()
    iss_lat = response["iss_position"]["latitude"]
    return iss_lat

#function to return the iss_long

def iss_long():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response = response.json()
    iss_long = response["iss_position"]["longitude"]
    return iss_long


#function to return the iss_lat and iss_long

def isslocation():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response = response.json()
    iss_lat = response["iss_position"]["latitude"]
    iss_long = response["iss_position"]["longitude"]
    return iss_lat, iss_long

    



