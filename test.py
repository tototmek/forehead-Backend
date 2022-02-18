import requests
import random

BASE="https://forehead-game-backend.herokuapp.com/"
#BASE = "http://127.0.0.1:5000/"

#data = {"likes": int(random.random()*120), "name":"Polish music", "views": int(random.random()*2137), "created_by": random.choice(['tototmek', 'hul0ng', 'johhny', 'Fredzio11', 'the Playlist Creator']), "tags": "music|rock|pop", "cards": "song1;band1|song2;band2|song3;band3|song4;band4|song5;band5|song6;band6|"}
        
# ADD GAME
#response = requests.post(BASE + "game/1", data)
#print(response.json())

# REGISTER USER
#response = requests.post(BASE + "signup", {"username":"h", "password":"h"})
#print(response.json())

# LOGIN
#response = requests.post(BASE + "login", {"username":"h", "password":"h"})
#print(response.json())

# CHECK IF USER EXISTS
#response = requests.get(BASE + "user/hulia")
#print(response.json())

# SEARCH
search_data = {"tags":"rock"}
response = requests.post(BASE + "search", search_data)
print(response.json())
print(len(response.json()))
