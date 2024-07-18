import time
import requests
from geopy.geocoders import Nominatim

def get_location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode("Your Address Here")
    return location.latitude, location.longitude

def send_location(server_url):
    while True:
        latitude, longitude = get_location()
        data = {'latitude': latitude, 'longitude': longitude}
        try:
            response = requests.post(f'{server_url}/update_location', json=data)
            if response.status_code == 200:
                print("Location sent successfully")
            else:
                print("Failed to send location")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(5)  # Send location every 5 seconds

if __name__ == '__main__':
    server_url = 'http://your-server-ip:5000'  # Replace with your server's IP address
    send_location(server_url)
