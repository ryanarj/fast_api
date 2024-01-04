from pydantic import BaseModel


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
