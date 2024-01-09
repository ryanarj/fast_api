from pydantic import BaseModel


class PlayerBase(BaseModel):
    name: str
    number: int
    position: str
    team: str


class StaffBase(BaseModel):
    name: str
    role: str


class TeamBase(BaseModel):
    name: str
    city: str
