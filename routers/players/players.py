from uuid import UUID

from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session

from db.connect import get_db
from schema.tables import Player
from schema.models import PlayerBase
from fastapi import APIRouter

router = APIRouter(prefix="/players", tags=["players"])


@router.get("/")
def index(db: Session = Depends(get_db)):
    players = db.query(Player).all()
    return {"players": players}


@router.get("/{player_id}")
def query_player_id(player_id: UUID, db: Session = Depends(get_db)):
    player = db.query(Player).filter(Player.id == player_id).first()
    if not player:
        raise HTTPException(status_code=404)
    return {"plauer": player}


@router.post("/add_players")
def add_player(player: PlayerBase, db: Session = Depends(get_db)):
    player = Player(
        name=player.name,
        position=player.position,
        team=player.team,
        number=player.number,
    )
    try:
        db.add(player)
        db.commit()
        db.refresh(player)
        return {"player": player}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
