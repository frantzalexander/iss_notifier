import requests
from datetime import datetime

MY_LAT = 45.516207
MY_LONG = -73.686547

def is_iss_overhead():
    response = requests.get(
        url = "http://api.open-notify.org/iss-now.json"
    )
    response.raise_for_status()
    data = response.json()

    position = data["iss_position"]


    iss_latitude = float(position["latitude"])
    iss_longitude = float(position["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
        return True
    
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "formatted": 0
    }

    response = requests.get(
        url = "https://api.sunrise-sunset.org/json",
        params = parameters
    )

    response.raise_for_status()
    sun_data = response.json()

    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True
    
is_iss_overhead()    
is_night()

    
if is_iss_overhead and is_night:
    print("You can see the ISS overhead!!")
