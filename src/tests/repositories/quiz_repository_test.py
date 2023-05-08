import unittest
from entities.puzzle import Puzzle
from entities.quiz import Quiz
from repositories.quiz_repository import QuizRepository

class TestQuizRepository(unittest.TestCase):

    def setUp(self):
        self.quiz_repository = QuizRepository()
        self.quiz_repository.delete_all()
    
    def test_save_quiz(self):
        puzzle1 = Puzzle("Test Puzzle 1", ["ONE", "TWO", "THREE", "FOUR", "FIVE"], 1)
        puzzle2 = Puzzle("Test Puzzle 2", ["SIX", "SEVEN", "EIGHT", "NINE", "TEN"], 1)
        quiz1 = Quiz("Test Quiz 1", [puzzle1])
        quiz2 = Quiz("Test Quiz 2", [puzzle2])

        self.quiz_repository.save_quiz(quiz1)
        self.quiz_repository.save_quiz(quiz2)

        names = self.quiz_repository.find_quiz_names()
        quiz1 = self.quiz_repository.find_quiz(names[0])
        quiz2 = self.quiz_repository.find_quiz(names[1])

        self.assertEqual(names, ["Test Quiz 1", "Test Quiz 2"])

        self.assertEqual(quiz1.puzzles[0].name, "Test Puzzle 1")
        self.assertEqual(quiz2.puzzles[0].name, "Test Puzzle 2")

        self.assertEqual(quiz1.puzzles[0].words, ["ONE", "TWO", "THREE", "FOUR", "FIVE"])
        self.assertEqual(quiz2.puzzles[0].words, ["SIX", "SEVEN", "EIGHT", "NINE", "TEN"])


    def test_delete_all(self):
        quizzes = self.quiz_repository.find_quiz_names()
        self.assertEqual(len(quizzes), 0)

    
    def test_find_all_names(self):
        puzzle1 = Puzzle("Test Puzzle 1", ["ONE", "TWO", "THREE", "FOUR", "FIVE"], 1)
        puzzle2 = Puzzle("Test Puzzle 2", ["SIX", "SEVEN", "EIGHT", "NINE", "TEN"], 1)
        quiz1 = Quiz("Test Quiz 1", [puzzle1])
        quiz2 = Quiz("Test Quiz 2", [puzzle2])

        self.quiz_repository.save_quiz(quiz1)
        self.quiz_repository.save_quiz(quiz2)

        names = self.quiz_repository.find_quiz_names()

        self.assertTrue("Test Quiz 1" in names)
        self.assertTrue("Test Quiz 2" in names)
        self.assertTrue(len(names) == 2)
