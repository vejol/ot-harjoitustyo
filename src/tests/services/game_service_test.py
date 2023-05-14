import unittest
from services.game_service import GameService
from entities.puzzle import Puzzle
from entities.quiz import Quiz

class TestGameService(unittest.TestCase):

    def setUp(self):
        puzzle1 = Puzzle("Test Puzzle 1", ["ONE", "TWO", "THREE", "FOUR", "FIVE"], 1)
        puzzle2 = Puzzle("Test Puzzle 2", ["SIX", "SEVEN", "EIGHT", "NINE", "TEN"], 2)
        quiz = Quiz("Test Quiz", [puzzle1, puzzle2])
        self.game_service = GameService(quiz)

    def test_add_point_add_points_right(self):
        self.game_service.add_point("team1")
        self.game_service.add_point("team1")
        self.assertEqual(self.game_service._points["team1"], 2)

        self.game_service.add_point("team2")
        self.assertEqual(self.game_service._points["team2"], 1)

    def test_dec_point_decrements_points_right(self):
        self.game_service.dec_point("team1")
        self.game_service.dec_point("team1")
        self.assertEqual(self.game_service._points["team1"], -2)

        self.game_service.dec_point("team2")
        self.assertEqual(self.game_service._points["team2"], -1)

    def test_get_word_returns_right_word(self):
        word = self.game_service.get_word(3)
        self.assertEqual(word, "FOUR")
    
    def test_next_puzzle_changes_current_puzzle(self):
        current = self.game_service._current_puzzle
        self.game_service.next_puzzle()
        new = self.game_service._current_puzzle
        self.assertFalse(current == new)
    
    def test_puzzles_available_gives_right_value(self):
        left = self.game_service.puzzles_available()
        self.assertTrue(left)

        self.game_service.next_puzzle()
        left = self.game_service.puzzles_available()
        self.assertFalse(left)

    def test_get_answer_gives_rigth_answer(self):
        answer = self.game_service.get_answer()
        self.assertEqual(answer, "Test Puzzle 1")

    def test_get_points_gives_right_values(self):
        team1_points = self.game_service.get_points("team1")
        team2_points = self.game_service.get_points("team2")
        self.assertEqual(team1_points, 0)
        self.assertEqual(team2_points, 0)

        self.game_service.add_point("team1")
        self.game_service.add_point("team1")
        self.assertEqual(self.game_service.get_points("team1"), 2)

        self.game_service.add_point("team2")
        self.assertEqual(self.game_service.get_points("team2"), 1)
    
    def test_red_word_points_right_words(self):
        red_words = self.game_service._red_words
        for i in range(6):
            result = self.game_service.red_word(i)
            self.assertEqual(result, i in red_words)
            