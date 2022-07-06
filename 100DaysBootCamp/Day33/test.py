import requests

response=requests.get(url="https://api.kanye.rest")

#print(response.status_code)
#print(response.raise_for_status())

data = response.json()
print(data['quote'])

