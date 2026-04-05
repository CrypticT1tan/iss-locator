import requests
import json
from geopy.geocoders import Nominatim, ArcGIS
import countryflag
from desktop_notifier import DesktopNotifier
import asyncio

def get_iss_coords() -> tuple:
    """
    Gets the current coordinates of the International Space Station
    :return: a tuple representing the latitude longitude coordinates of the ISS
    """
    iss_json = requests.get("http://api.open-notify.org/iss-now.json").json()
    iss_position = iss_json["iss_position"]
    iss_lat = iss_position["latitude"]
    iss_long = iss_position["longitude"]
    return iss_lat, iss_long

def get_location(lat, long) -> str:
    """
    Converts latitude and longitude coordinates to a location
    :param lat: the latitude coordinate
    :param long: the longitude coordinate
    :return: a string representing the location of the given coordinates
    """
    # Try seeing if ISS is over land (specifically a country)
    geolocator = Nominatim(user_agent="ISS-Locator")
    location = geolocator.reverse((lat, long), language="en")
    if not location: # If the location is not over land 
        # Find out what ocean/body of water it is currently over
        geolocator = ArcGIS()
        location = geolocator.reverse((lat, long))
    return location

async def notify(coords, location) -> None:
    """
    Notify the user via desktop about the current location of the ISS
    :param coords: the current coordinates of the ISS
    :param location: the current location of the ISS
    """
    notifier = DesktopNotifier(app_name="ISS Locator")
    await notifier.send(
        title="ISS Current Location", 
        message=f"{location}\nCoordinates: {coords[0]}, {coords[1]}"
        )

def main():
    iss_coords = get_iss_coords() # Get the coordinates of the ISS
    iss_loc = get_location(iss_coords[0], iss_coords[1]) # Convert coordinates to a location
    asyncio.run(notify(iss_coords, iss_loc)) 

if __name__ == "__main__":
    main()