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
        self.game_service.add_point_team1()
        self.assertEqual(self.game_service.team1_points, 1)
