from uuid import UUID

from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from db.connect import get_db
from schema.tables import Player
from schema.models import PlayerBase, PlayerPromptBase
from fastapi import APIRouter

from services.laminiLMM.lamini import LaminiService
from services.players.players import PlayerService

router = APIRouter(prefix="/players", tags=["players"])


@router.get("/")
def index(db: Session = Depends(get_db)):
    players = db.query(Player).all()
    return {"players": players}


@router.get("/{player_id}")
def query_player_id(player_id: UUID, db: Session = Depends(get_db)):
    player = PlayerService.get_player_by_id(player_id, db)
    if not player:
        raise HTTPException(status_code=404)
    return {"player": player}


@router.post("/add_players")
def add_player(player: PlayerBase, db: Session = Depends(get_db)):
    player = Player(
        name=player.name,
        position=player.position,
        team=player.team,
        number=player.number,
    )
    try:
        return PlayerService.commit_player(player, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/add_players")
def add_player(player: PlayerBase, db: Session = Depends(get_db)):
    player = Player(
        name=player.name,
        position=player.position,
        team=player.team,
        number=player.number,
    )
    try:
        return PlayerService.commit_player(player, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/prompt_player")
def prompt_player(player_prompt: PlayerPromptBase):
    prompt = player_prompt.prompt
    lamini = LaminiService()
    try:
        if 'nba' in prompt.lower():
            return lamini.generate_answer_from_prompt(prompt)
        else:
            return 'Cannot prompt this request.'
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

