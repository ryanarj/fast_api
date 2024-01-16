from routers.players.players import add_player
from schema.models import PlayerBase
from schema.tables import Player
from services.players.players import commit_player, get_player_by_id


def test_create_player():
    player = Player(name="<NAME>", number=12, position="player", team="test")
    player = commit_player(player)
    player = player["player"]
    test_player = get_player_by_id(player.id)
    assert player.name == test_player.name
    assert player.number == test_player.number
    assert player.position == test_player.position
    assert player.team == test_player.team
