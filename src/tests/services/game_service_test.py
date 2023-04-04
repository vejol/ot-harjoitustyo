import unittest
from services.game_service import GameService

class TestGameService(unittest.TestCase):

    def setUp(self):
        self.game_service = GameService()

    def test_turn_default_value_is_1(self):
        self.assertEqual(self.game_service.turn, 1)
    
    def test_turn_changes_to_2(self):
        self.game_service.change_turn()
        self.assertEqual(self.game_service.turn, 2)

    def test_turn_changes_back_to_1(self):
        self.game_service.change_turn()
        self.game_service.change_turn()
        self.assertEqual(self.game_service.turn, 1)

    
