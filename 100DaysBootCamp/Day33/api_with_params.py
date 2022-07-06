import requests
import datetime as dt
import  smtplib
import  time

MY_EMAIL = "ateya.api@gmail.com"
MY_PASSWORD = "@ChampionArrey1994"
MY_LAT = "35.653140"
MY_LNG = "-97.481510"



def is_iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if MY_LNG-5 <= longitude <= MY_LNG +5 and MY_LAT -5 <= latitude <= MY_LAT +5:
        return True



def is_night():
    paramters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=paramters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data['results']["sunset"].split("T")[1].split(":")[0])

    current_time = dt.datetime.now().hour
    if sunrise <= current_time or current_time <=sunset:
        return True

while True:
    time.sleep((60))
    if is_night() and is_iss_overhead():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login((MY_EMAIL, MY_PASSWORD))
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look up \n\n The ISS is above you in the sky."
        )



"""
    Challenge:
        - If the ISS is close to my current position
        and it's currently dark, then send me an email to tell me to look up.
        BONUS: run the code every 60 seconds
"""