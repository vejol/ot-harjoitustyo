import unittest
from services.game_service import GameService
from entities.puzzle import Puzzle
from entities.quiz import Quiz

class TestGameService(unittest.TestCase):

    def setUp(self):
        puzzle = Puzzle("Test Puzzle", ["one", "two", "three", "four", "five"], 1)
        quiz = Quiz("Test Quiz", [puzzle])
        self.game_service = GameService(quiz)

    def test_adding_point_to_team1_works(self):
        self.game_service.change_points("team1", 2)
        self.assertEqual(self.game_service._points["team1"], 2)

    def test_decrementing_point_from_team2_works(self):
        self.game_service.change_points("team2", -2)
        self.assertEqual(self.game_service._points["team2"], -2)
