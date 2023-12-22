import requests
from datetime import datetime

today = datetime.today().strftime("%Y%m%d")

USERNAME = "bakuvi"
TOKEN = "Hidden"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_config = {
    "id": GRAPH_ID,
    "name": "Walking records",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
pixel_params = {
    "date": today,
    "quantity": "7.71",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# response= requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)
