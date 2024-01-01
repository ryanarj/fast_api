import requests

from main import Player

print(
    requests.get("http://127.0.0.1:8000/players/1").json()
)

print(
    requests.post("http://127.0.0.1:8000/add_players", json={
        "id": 7, "name": "Carmelo Anthony", "number": 7, "position": 'PF', "team": 'Knicks'
    }).json()
)
