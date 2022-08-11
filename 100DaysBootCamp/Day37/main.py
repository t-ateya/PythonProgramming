
import requests
from datetime import datetime

USERNAME = "ateya";
TOKEN = "123542agreatninja"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
    "thanksCode":"Thank you very much"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" :"graph1",
    "name" : "My Coding Graph",
    "unit" : "Hours",
    "type": "int",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN" : TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

#print(response.text)

post_value_endpoint = f"{graph_endpoint}/{graph_config['id']}"

today = datetime.now();
#today = datetime(year= 2022, month=8, day=15)
graph_data = {
    "date" : today.strftime("%Y%m%d"),
    #"quantity": "15"
    "quantity": input("How many hours do you work per day: ")
}

response = requests.post(url=post_value_endpoint, json=graph_data, headers=headers);
#print(response.text)

#Updating pixel

update_endpoint = f"{post_value_endpoint}/{today.strftime('%Y%m%d')}"

new_data = {
    "quantity": "20"
}

response = requests.put(url=update_endpoint, json=new_data, headers=headers)

#print(response.text)

#Delete pixel data
delete_endpoint = f"{update_endpoint}";

del_response = requests.delete(url=delete_endpoint, headers=headers)
print(del_response.text)

