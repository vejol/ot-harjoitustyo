import unittest
from entities.puzzle import Puzzle
from entities.quiz import Quiz
from repositories.quiz_repository import QuizRepository

class TestQuizRepository(unittest.TestCase):

    def setUp(self):
        self.quiz_repository = QuizRepository()
        self.quiz_repository.delete_all()
    
    def test_save(self):
        puzzle1 = Puzzle("Test Puzzle 1", ["one", "two", "three", "four", "five"], 1)
        puzzle2 = Puzzle("Test Puzzle 2", ["six", "seven", "eight", "nine", "ten"], 1)
        quiz1 = Quiz("Test Quiz 1", [puzzle1])
        quiz2 = Quiz("Test Quiz 2", [puzzle2])

        self.quiz_repository.save(quiz1)
        self.quiz_repository.save(quiz2)

        names = self.quiz_repository.find_all_names()
        quiz1 = self.quiz_repository.find_quiz(names[0])
        quiz2 = self.quiz_repository.find_quiz(names[1])

        self.assertEqual(names, ["Test Quiz 1", "Test Quiz 2"])

        self.assertEqual(quiz1.puzzles[0].name, "Test Puzzle 1")
        self.assertEqual(quiz2.puzzles[0].name, "Test Puzzle 2")

        self.assertEqual(quiz1.puzzles[0].words, ["one", "two", "three", "four", "five"])
        self.assertEqual(quiz2.puzzles[0].words, ["six", "seven", "eight", "nine", "ten"])


    def test_delete_all(self):
        quizzes = self.quiz_repository.find_all_names()
        self.assertEqual(len(quizzes), 0)

    
    def test_find_all_names(self):
        puzzle1 = Puzzle("Test Puzzle 1", ["one", "two", "three", "four", "five"], 1)
        puzzle2 = Puzzle("Test Puzzle 2", ["six", "seven", "eight", "nine", "ten"], 1)
        quiz1 = Quiz("Test Quiz 1", [puzzle1])
        quiz2 = Quiz("Test Quiz 2", [puzzle2])

        self.quiz_repository.save(quiz1)
        self.quiz_repository.save(quiz2)

        names = self.quiz_repository.find_all_names()

        self.assertTrue(len(names) == 2)
        self.assertEqual(quiz1.puzzles[0].name, "Test Puzzle 1")
        self.assertEqual(quiz2.puzzles[0].name, "Test Puzzle 2")
