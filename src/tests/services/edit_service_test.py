import unittest
from entities.puzzle import Puzzle
from entities.quiz import Quiz
from tests.services.management_service_test import FakeQuizRepository
from services.edit_service import (
    EditService, 
    MultipleWordsError,
    NoPuzzleNameError,
    NoPuzzlesError,
    NoPuzzleWordError,
    NoQuizNameError,
    PuzzleNameLenghtError,
    PuzzleWordLenghtError,
    QuizExistError
)

class TestEditService(unittest.TestCase):
    """Tämä testiluokka testaa EditService-luokkaa tilanteessa, jossa 
       käyttäjä haluaa luoda uuden visailun. Tässä tapauksessa luokan
       suojattu atribuutti self._quiz sisältää aluksi tyhjän Quiz-olion.
    """

    def setUp(self):
        self.repository  = FakeQuizRepository()

        puzzle1 = Puzzle("Test Puzzle 1", ["ONE", "TWO", "THREE", "FOUR", "FIVE"], 1)
        puzzle2 = Puzzle("Test Puzzle 2", ["SIX", "SEVEN", "EIGHT", "NINE", "TEN"], 2)
        self.quiz = Quiz("Test Quiz", [puzzle1, puzzle2])
        self.repository.save_quiz(self.quiz)
        
        self.edit_service1 = EditService(Quiz("", []), self.repository)
        self.edit_service2 = EditService(self.quiz, self.repository)

    def test_get_name_return_right_values(self):
        name1 = self.edit_service1.get_name()
        name2 = self.edit_service2.get_name()

        self.assertEqual(name1, "")
        self.assertEqual(name2, "Test Quiz")

    def test_set_name_raises_error_if_name_already_exist(self):
        self.repository.save_quiz(self.quiz)
        
        self.assertRaises(
            QuizExistError,
            lambda: self.edit_service1.set_name("Test Quiz")
        )
    
    def test_set_name_raises_error_if_name_empty(self):
        self.assertRaises(
            NoQuizNameError,
            lambda: self.edit_service1.set_name("")
        )

        self.assertRaises(
            NoQuizNameError,
            lambda: self.edit_service1.set_name("   ")
        )

    def test_set_name_sets_right_value(self):
        self.edit_service1.set_name("Test")
        self.assertEqual(self.edit_service1._quiz.name, "Test")

    def test_get_puzzles(self):
        puzzles1 = self.edit_service1.get_puzzles()
        puzzles2 = self.edit_service2.get_puzzles()

        self.assertEqual(len(puzzles1), 0)
        self.assertEqual(len(puzzles2), 2)
        
        self.assertTrue(puzzles2[0].name == "Test Puzzle 1")
        self.assertTrue(puzzles2[1].name == "Test Puzzle 2")
    
    def test_add_puzzle_raises_error_if_no_puzzle_name(self):
        self.assertRaises(
            NoPuzzleNameError,
            lambda: self.edit_service1.add_puzzle("", ["a","b","c","d","e"])
        )

        self.assertRaises(
            NoPuzzleNameError,
            lambda: self.edit_service1.add_puzzle(" ", ["a","b","c","d","e"])
        )

    def test_add_puzzle_raises_error_if_puzzle_name_too_long(self):
        self.assertRaises(
            PuzzleNameLenghtError,
            lambda: self.edit_service1.add_puzzle("A" * 120, ["a","b","c","d","e"])
        )

    def test_add_puzzle_raises_error_if_puzzle_word_empty(self):
        self.assertRaises(
            NoPuzzleWordError,
            lambda: self.edit_service1.add_puzzle("Puzzle", ["","b","c","d","e"])
        )

        self.assertRaises(
            NoPuzzleWordError,
            lambda: self.edit_service1.add_puzzle("Puzzle", [" ","b","c","d","e"])
        )

    def test_add_puzzle_raises_error_if_puzzle_word_is_not_single_word(self):
        self.assertRaises(
            MultipleWordsError,
            lambda: self.edit_service1.add_puzzle("Puzzle", ["a","x and y","c","d","e"])
        )

    def test_add_puzzle_raises_error_if_puzzle_word_is_too_long(self):
        self.assertRaises(
            PuzzleWordLenghtError,
            lambda: self.edit_service1.add_puzzle("Puzzle", ["a"*15,"b","c","d","e"])
        )

    def test_add_puzzle_works_if_no_error(self):
        self.edit_service1.add_puzzle("Puzzle", ["A","B","C","D","E"])
        puzzles = self.edit_service1.get_puzzles()

        self.assertEqual(len(puzzles), 1)
        self.assertEqual(puzzles[0].name, "Puzzle")
        self.assertEqual(puzzles[0].words, ["A","B","C","D","E"])

    def test_remove_puzzle(self):
        self.edit_service2.remove_puzzle(0)

        self.assertEqual(len(self.edit_service2.get_puzzles()), 1)
        self.assertEqual(self.edit_service2._quiz.puzzles[0].name, "Test Puzzle 2")

    def test_save_quiz_raises_error_if_no_puzzles(self):
        self.assertRaises(
            NoPuzzlesError,
            lambda: self.edit_service1.save_quiz()
        )

    def test_save_quiz_works_if_no_error(self):
        self.edit_service1.set_name("Testing")
        self.edit_service1.add_puzzle("Test Puzzle", ["A","B","C","D","E"])
        self.edit_service1.save_quiz()
        
        quiz = self.repository.find_quiz("Testing")
        self.assertEqual(quiz.name, "Testing")
        self.assertEqual(quiz.puzzles[0].name, "Test Puzzle")
        self.assertEqual(quiz.puzzles[0].words, ["A","B","C","D","E"])

    def test_save_quiz_works_if_quiz_name_changes(self):
        self.edit_service2.set_name("Testing")
        self.edit_service2.save_quiz()
        
        quiz = self.repository.find_quiz("Testing")
        self.assertEqual(len(quiz.puzzles), 2)
        self.assertEqual(quiz.puzzles[0].name, "Test Puzzle 1")
        self.assertEqual(quiz.puzzles[1].name, "Test Puzzle 2")
        self.assertEqual(quiz.puzzles[0].words, ["ONE", "TWO", "THREE", "FOUR", "FIVE"])
        self.assertEqual(quiz.puzzles[1].words, ["SIX", "SEVEN", "EIGHT", "NINE", "TEN"])
        