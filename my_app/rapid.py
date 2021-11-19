# import requests

# url = "https://community-hacker-news-v1.p.rapidapi.com/item/8863.json"

# querystring = {"print":"pretty"}

# headers = {
#     'x-rapidapi-host': "community-hacker-news-v1.p.rapidapi.com",
#     'x-rapidapi-key': "3bc1f43f10msh441ba1dea621333p1e14a0jsn7a5e4edccc6f"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

import requests

url = "https://google-news.p.rapidapi.com/v1/topic_headlines"

querystring = {"lang":"en","country":"US","topic":"technology"}

headers = {
    'x-rapidapi-host': "google-news.p.rapidapi.com",
    'x-rapidapi-key': "3bc1f43f10msh441ba1dea621333p1e14a0jsn7a5e4edccc6f"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)