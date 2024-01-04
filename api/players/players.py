from fastapi import HTTPException

from api.core.FastApiService import FastApiService
from schema.models import Player

players = {
    0: Player(id=0, name="John Starks", number=3, position="SG", team="Knicks"),
    1: Player(id=1, name="Patrick Ewing", number=33, position="C", team="Knicks"),
    2: Player(id=2, name="Charles Oakley", number=34, position="PF", team="Knicks"),
}

app = FastApiService().app


@app.get("/")
def index():
    return {"players": players}


@app.get("/players/{player_id}")
def query_player_id(player_id: int):
    if not players.get(player_id):
        raise HTTPException(status_code=404)
    return players.get(player_id)


@app.post("/add_players")
def query_player_id(player: Player):
    if player.id in players:
        raise HTTPException(status_code=400)
    players[player.id] = player
    return {"players": players}
