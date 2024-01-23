from pydantic import BaseModel


class PlayerBase(BaseModel):
    name: str
    number: int
    position: str
    team: str


class PlayerPromptBase(BaseModel):
    prompt: str


class StaffBase(BaseModel):
    name: str
    role: str


class TeamBase(BaseModel):
    name: str
    city: str
