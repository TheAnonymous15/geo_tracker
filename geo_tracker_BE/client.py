import time
from gps3 import gps3

def send_location():
    gps_socket = gps3.GPSDSocket()
    data_stream = gps3.DataStream()

    try:
        for new_data in gps_socket:
            if new_data:
                data_stream.unpack(new_data)
                if data_stream.TPV['lat'] != 'n/a' and data_stream.TPV['lon'] != 'n/a':
                    latitude = data_stream.TPV['lat']
                    longitude = data_stream.TPV['lon']
                    print(f"Latitude: {latitude}, Longitude: {longitude}")
                    return  # Exit after retrieving one set of coordinates
            time.sleep(0.5)  # Adjust sleep time as needed
    except Exception as e:
        print(f"Error retrieving GPS data: {e}")

if __name__ == "__main__":
    send_location()
