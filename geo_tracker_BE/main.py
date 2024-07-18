import time
import requests
from fastapi import FastAPI, BackgroundTasks
from geopy.geocoders import Nominatim

app = FastAPI()
background_tasks = BackgroundTasks()  # Define background_tasks instance

def get_location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode("Nairobi")
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

def send_location():
    server_url = 'http://0.0.0.0:8000/update_location/'  # Django server URL
    while True:
        latitude, longitude = get_location()
        if latitude is not None and longitude is not None:
            data = {'latitude': latitude, 'longitude': longitude}
            try:
                response = requests.post(server_url, json=data)
                if response.status_code == 200:
                    print("Location sent successfully")
                else:
                    print("Failed to send location")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Failed to get location")
        time.sleep(5)  # Send location every 5 seconds

@app.on_event("startup")
def startup_event():
    background_tasks.add_task(send_location)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8001)
