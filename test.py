from urllib import response
import requests

BASE="https://foreheadgameapi.netlify.app/"

# data = [{"likes": 78, "name":"Best ballads", "views": 123, "created_by": "YoMama", "tags": "music,rock", "cards": 'gg,g,ds,aasd,f'},
#    {"likes": 73458, "name":"Only the best", "views": 55, "created_by": "tototmek", "tags": "music", "cards": 'gg,g,ds,aasd,f'},
#    {"likes": 7238, "name":"Polskie hity", "views": 66, "created_by": "Johnny", "tags": "music,capy", "cards": 'gg,g,ds,aasd,f'},
#    {"likes": 73458, "name":"Just music", "views": 125, "created_by": "tototmek", "tags": "music", "cards": 'gg,g,ds,aasd,f'},
#    {"likes": 7238, "name":"English hits", "views": 231, "created_by": "Gustaw", "tags": "music,sztos", "cards": 'gg,g,ds,aasd,f'},
#    {"likes": 73458, "name":"Just Best songs", "views": 110, "created_by": "tototmek", "tags": "music,sztos,rock", "cards": 'gg,g,ds,aasd,f'},
#    {"likes": 7238, "name":"Metal", "views": 125, "created_by": "Johnny", "tags": "music,capy,rock", "cards": 'gg,g,ds,aasd,f'},
#        ]

# for i in range(len(data)):
#     requests.put(BASE + "game/1", data[i])

# requests.put(BASE + "user/tototmek")


#search_data = {"name":"rock"}
#response = requests.get(BASE + "search", search_data)
#print(response.json())
#print(len(response.json()))

response = requests.get(BASE + "game/1")
print(response.json())