import uuid

from sqlalchemy import Column, UUID, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from db.connect import engine

Base = declarative_base()


class Player(Base):
    __tablename__ = "players"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    number = Column(Integer)
    position = Column(String)
    team = Column(String)


Base.metadata.create_all(engine)
