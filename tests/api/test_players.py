from api.players.players import add_player
from schema.models import Player


def test_query_player_id():
    player = Player(id=12, name="<NAME>", number=12, position="player", team="test")
    players = add_player(player)
    players = players["players"]
    test_player = players.get(player.id)
    assert player.name == test_player.name
    assert player.number == test_player.number
    assert player.position == test_player.position
    assert player.team == test_player.team
