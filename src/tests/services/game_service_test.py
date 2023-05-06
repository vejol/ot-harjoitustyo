import unittest
from services.game_service import GameService
from entities.puzzle import Puzzle
from entities.quiz import Quiz

class TestGameService(unittest.TestCase):

    def setUp(self):
        puzzle = Puzzle("Test Puzzle", ["one", "two", "three", "four", "five"], 1)
        quiz = Quiz("Test Quiz", [puzzle])
        self.game_service = GameService(quiz)

    def test_adding_point_works(self):
        self.game_service.add_point("team1")
        self.game_service.add_point("team1")
        self.assertEqual(self.game_service._points["team1"], 2)

        self.game_service.add_point("team2")
        self.assertEqual(self.game_service._points["team2"], 1)

    def test_decrementing_point_works(self):
        self.game_service.dec_point("team1")
        self.game_service.dec_point("team1")
        self.assertEqual(self.game_service._points["team1"], -2)

        self.game_service.dec_point("team2")
        self.assertEqual(self.game_service._points["team2"], -1)

    def test_reveal_field_works(self):
        self.assertEqual(self.game_service._revealed[3], False)
        self.game_service.reveal_field(3)
        self.assertEqual(self.game_service._revealed[3], True)
