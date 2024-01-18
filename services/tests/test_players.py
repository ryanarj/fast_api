import unittest

from schema.tables import Player
from services.players.players import PlayerService


class TestPlayerService(unittest.TestCase):
    def test_create_and_get_player(self):
        player = Player(name="<NAME>", number=12, position="player", team="test")
        player = PlayerService.commit_player(player)
        player = player["player"]
        test_player = PlayerService.get_player_by_id(player.id)
        self.assertEquals(player.name, test_player.name)
        self.assertEquals(player.number, test_player.number)
        self.assertEquals(player.position, test_player.position)
        self.assertEquals(player.team, test_player.team)
