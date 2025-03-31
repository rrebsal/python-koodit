import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)

if response.status_code == 200:
    joke = response.json().get("value")
    print(joke)
else:
    print("Failed to retrieve a joke.")