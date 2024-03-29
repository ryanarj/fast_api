from uuid import UUID

from db.connect import Session, get_db
from schema.tables import Player


class PlayerService:
    @staticmethod
    def commit_player(player: Player, db: Session = None):
        db = db if db else next(get_db())
        try:
            db.add(player)
            db.commit()
            db.refresh(player)
            return {"player": player}
        except Exception as e:
            raise e

    @staticmethod
    def get_player_by_id(player_id: UUID, db: Session = None):
        db = db if db else next(get_db())
        try:
            return db.query(Player).filter(Player.id == player_id).first()
        except Exception as e:
            raise e
