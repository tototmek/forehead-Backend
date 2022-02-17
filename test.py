import requests

BASE="https://forehead-game-backend.herokuapp.com/"
BASE = "http://127.0.0.1:5000/"

# data = [{"likes": 78, "name":"Best ballads", "views": 123, "created_by": "YoMama", "tags": "music,rock", "cards": 'gg,g,ds,aasd,f'},
#    {"likes": 73458, "name":"Only the best", "views": 55, "created_by": "tototmek", "tags": "music", "cards": 'gg,g,ds,aasd,f'},
#    {"likes": 7238, "name":"Polskie hity", "views": 66, "created_by": "Johnny", "tags": "music,capy", "cards": 'gg,g,ds,aasd,f'},
#    {"likes": 73458, "name":"Just music", "views": 125, "created_by": "tototmek", "tags": "music", "cards": 'gg,g,ds,aasd,f'},
#    {"likes": 7238, "name":"English hits", "views": 231, "created_by": "Gustaw", "tags": "music,sztos", "cards": 'gg,g,ds,aasd,f'},
#    {"likes": 73458, "name":"Just Best songs", "views": 110, "created_by": "tototmek", "tags": "music,sztos,rock", "cards": 'gg,g,ds,aasd,f'},
#    {"likes": 7238, "name":"Metal", "views": 125, "created_by": "Johnny", "tags": "music,capy,rock", "cards": 'gg,g,ds,aasd,f'},
#        ]

# ADD GAME
# for i in range(len(data)):
#     requests.put(BASE + "game/1", data[i])

# REGISTER USER
response = requests.post(BASE + "login", {"username":"karlositos231", "password":"karlos21_37"})
print(response.json())

# LOGIN
#response = requests.get(BASE + "login", {"username":"karlos", "password":"kalfros21_37"})
#print(response.json())

# CHECK IF USER EXISTS
#response = requests.get(BASE + "user/hulia")
#print(response.json())

# SEARCH
# search_data = {"tags":"rock"}
# response = requests.get(BASE + "search", search_data)
# print(response.json())
# print(len(response.json()))
