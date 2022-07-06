import requests

response=requests.get(url="http://api.open-notify.org/iss-now.json")
response=requests.get(url="http://api.open-notify.org/iss-now.json")
#print(response.status_code)
#print(response.raise_for_status())

data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (longitude,latitude)
print(iss_position)

