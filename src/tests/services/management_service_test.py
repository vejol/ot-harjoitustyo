import unittest
from services.management_service import ManagementService
from entities.puzzle import Puzzle
from entities.quiz import Quiz

class FakeQuizRepository:

    def __init__(self):
        self.quizzes = []

    def delete_all(self):
        self.quizzes = []
    
    def delete_quiz(self, quiz_name):
        for quiz in self.quizzes:
            if quiz.name == quiz_name:
                self.quizzes.remove(quiz)
    
    def find_all_quizzes(self):
        result = {}
        for quiz in self.quizzes:
            result[quiz.name] = quiz
        return result
    
    def find_quiz_names(self):
        return [quiz.name for quiz in self.quizzes]
    
    def find_quiz(self, name):
        result = None
        for quiz in self.quizzes:
            if quiz.name == name:
                result = quiz
        return result
    
    def save_quiz(self, quiz: Quiz):
        self.quizzes.append(quiz)
    
    def update_quiz(self, updated_quiz, old_name):
        for quiz in self.quizzes:
            if quiz.name == old_name:
                self.quizzes.remove(quiz)
        self.quizzes.append(updated_quiz)

class TestManagementService(unittest.TestCase):

    def setUp(self):
        self.management_service = ManagementService(FakeQuizRepository())

        puzzle1 = Puzzle("Test Puzzle 1", ["ONE", "TWO", "THREE", "FOUR", "FIVE"], 1)
        puzzle2 = Puzzle("Test Puzzle 2", ["SIX", "SEVEN", "EIGHT", "NINE", "TEN"], 2)
        self.test_quiz1 = Quiz("Test Quiz 1", [puzzle1, puzzle2])

        puzzle3 = Puzzle("Test Puzzle 3", ["WISE", "MEN", "SAY", "ONLY", "FOOLS"], 1)
        puzzle4 = Puzzle("Test Puzzle 4", ["AND", "I", "THINK", "TO", "MYSELF"], 2)
        self.test_quiz2 = Quiz("Test Quiz 2", [puzzle3, puzzle4])

    def test_add_quiz(self):
        self.management_service.add_quiz(self.test_quiz1)
        quizzes = self.management_service.find_all_quizzes()
        self.assertEqual(len(quizzes), 1)
        self.assertEqual(quizzes["Test Quiz 1"], self.test_quiz1)

    def test_find_all_quizzes(self):
        quizzes = self.management_service.find_all_quizzes()
        self.assertEqual(len(quizzes), 0)

        self.management_service.add_quiz(self.test_quiz1)
        self.management_service.add_quiz(self.test_quiz2)
        quizzes = self.management_service.find_all_quizzes()
        
        self.assertEqual(len(quizzes), 2)
        self.assertEqual(quizzes["Test Quiz 1"], self.test_quiz1)
        self.assertEqual(quizzes["Test Quiz 2"], self.test_quiz2)

    def test_delete_quiz(self):
        self.management_service.add_quiz(self.test_quiz1)
        self.management_service.add_quiz(self.test_quiz2)
        
        self.management_service.delete_quiz("Test Quiz 1")
        quizzes = self.management_service.find_all_quizzes()
        self.assertEqual(len(quizzes), 1)
        self.assertEqual(quizzes["Test Quiz 2"], self.test_quiz2)

        self.management_service.delete_quiz("Test Quiz 2")
        quizzes = self.management_service.find_all_quizzes()
        self.assertEqual(len(quizzes), 0)
    
    def test_add_default_quizzes(self):
        self.management_service.add_default_quizzes()
        quizzes = self.management_service.find_all_quizzes()
        quiz_names = self.management_service.get_quiz_names()

        self.assertEqual(len(quizzes), 2)
        self.assertTrue("Suomivisa" in quiz_names)
        self.assertTrue("Joululauluvisa" in quiz_names)


    def test_get_quiz(self):
        self.management_service.add_quiz(self.test_quiz1)
        self.management_service.add_quiz(self.test_quiz2)

        quiz1 = self.management_service.get_quiz("Test Quiz 1")
        quiz2 = self.management_service.get_quiz("Test Quiz 2")

        self.assertEqual(quiz1, self.test_quiz1)
        self.assertEqual(quiz2, self.test_quiz2)