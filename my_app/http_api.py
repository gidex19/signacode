import json
import requests
#response = requests.get("http://api.open-notify.org/astros.json")
response = requests.get("https://newsapi.org/v2/everything?q=keyword&apiKey=5cfc4aeaa97d4e58a66e5d19bcc1953a")
data = response.text
datas = json.loads(data)
print(data[0])