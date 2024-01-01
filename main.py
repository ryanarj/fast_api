from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Category(Enum):
    PLAYERS = 'players'
    STAFF = 'staff'


class Player(BaseModel):
    id: int
    name: str
    number: int
    position: str
    team: str


class Staff(BaseModel):
    name: str
    role: str


class Team(BaseModel):
    name: str
    city: str


players = {
    0: Player(
        id=0,
        name="John Starks",
        number=3,
        position="SG",
        team="Knicks"
    ),
    1: Player(
        id=1,
        name="Patrick Ewing",
        number=33,
        position="C",
        team="Knicks"
    ),
    2: Player(
        id=2,
        name="Charles Oakley",
        number=34,
        position="PF",
        team="Knicks"
    )
}


@app.get('/')
def index():
    return {"players": players}


@app.get('/player/{player_id}')
def query_player_id(player_id):
    return players.get(player_id)

