import unittest
from entities.puzzle import Puzzle
from entities.quiz import Quiz
from repositories.quiz_repository import QuizRepository

class TestQuizRepository(unittest.TestCase):

    def setUp(self):
        self.repository = QuizRepository()
        self.repository.delete_all()
    
        puzzle1 = Puzzle("Test Puzzle 1", ["ONE", "TWO", "THREE", "FOUR", "FIVE"], 1)
        puzzle2 = Puzzle("Test Puzzle 2", ["SIX", "SEVEN", "EIGHT", "NINE", "TEN"], 1)
        self.quiz1 = Quiz("Test Quiz 1", [puzzle1])
        self.quiz2 = Quiz("Test Quiz 2", [puzzle2])

    def test_save_quiz(self):
        self.repository.save_quiz(self.quiz1)
        self.repository.save_quiz(self.quiz2)

        names = self.repository.find_quiz_names()
        quiz1 = self.repository.find_quiz(names[0])
        quiz2 = self.repository.find_quiz(names[1])

        self.assertEqual(names, ["Test Quiz 1", "Test Quiz 2"])
        self.assertEqual(quiz1.puzzles[0].name, "Test Puzzle 1")
        self.assertEqual(quiz2.puzzles[0].name, "Test Puzzle 2")

        self.assertEqual(quiz1.puzzles[0].words, ["ONE", "TWO", "THREE", "FOUR", "FIVE"])
        self.assertEqual(quiz2.puzzles[0].words, ["SIX", "SEVEN", "EIGHT", "NINE", "TEN"])

    def test_update_quiz(self):
        self.repository.save_quiz(self.quiz1)
        self.quiz1.name = "New Name"
        self.repository.update_quiz(self.quiz1, "Test Quiz 1")

        quizzes = self.repository.find_all_quizzes()
        self.assertTrue("New Name" in quizzes)

    def test_delete_all(self):
        quizzes = self.repository.find_quiz_names()
        self.assertEqual(len(quizzes), 0)
    
    def test_delete_quiz(self):
        self.repository.save_quiz(self.quiz1)
        quizzes = self.repository.find_all_quizzes()
        self.assertEqual(len(quizzes), 1)

        self.repository.delete_quiz(self.quiz1)
        quizzes = self.repository.find_all_quizzes()
        self.assertEqual(len(quizzes), 0)
    
    def test_find_all_names(self):
        self.repository.save_quiz(self.quiz1)
        self.repository.save_quiz(self.quiz2)

        names = self.repository.find_quiz_names()
        self.assertTrue("Test Quiz 1" in names)
        self.assertTrue("Test Quiz 2" in names)
        self.assertTrue(len(names) == 2)

    def test_find_all_quizzes(self):
        self.repository.save_quiz(self.quiz1)
        self.repository.save_quiz(self.quiz2)

        quizzes = self.repository.find_all_quizzes()
        self.assertTrue("Test Quiz 1" in quizzes)
        self.assertTrue("Test Quiz 2" in quizzes)


