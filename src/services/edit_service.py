import copy
from entities.puzzle import Puzzle
from entities.quiz import Quiz
from repositories.quiz_repository import QuizRepository
from services.management_service import management_service


class EditService:

    def __init__(self, old_quiz: Quiz):
        self._repository = QuizRepository()
        self._old_quiz = old_quiz
        self._quiz = copy.deepcopy(old_quiz)

    def get_name(self):
        return self._quiz.name

    def set_name(self, name: str):
        name = name.strip()

        if name == "":
            raise NoQuizNameError("Quiz name is missing.")

        old_name = self._old_quiz.name
        quiz_names = management_service.get_quiz_names()

        if name in quiz_names and name != old_name:
            raise QuizExistError("A quiz with same name already exists.")

        self._quiz.name = name

    def get_puzzles(self):
        return self._quiz.puzzles

    def add_puzzle(self, user_input):
        name = user_input.pop(0)
        words = user_input
        puzzle = Puzzle(name, words)

        self._quiz.puzzles.append(puzzle)

    def remove_puzzle(self, index):
        self._quiz.puzzles.pop(index)

    def save_quiz(self):
        if self._old_quiz.name != "":
            self._repository.delete_quiz(self._old_quiz)

        self._repository.save_quiz(self._quiz)


class QuizExistError(Exception):
    pass

class NoQuizNameError(Exception):
    pass
