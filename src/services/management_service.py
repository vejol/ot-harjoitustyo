from repositories.quiz_repository import QuizRepository
from entities.puzzle import Puzzle
from entities.quiz import Quiz

class ManagementService:

    def __init__(self):
        self._quiz_repository = QuizRepository()


    def add_quiz(self, quiz):
        self._quiz_repository.save(quiz)


    def add_default_quizzes(self):
        puzzle1 = Puzzle("Maamme-laulu", ["laaksoa", "ei", "kukkulaa", "ei", "vettä"], 1)
        puzzle2 = Puzzle("Petteri Punakuono", ["pitkä", "on", "taival", "valoton,", "Petteri"], 1)

        self.add_quiz(Quiz("Suomivisa", [puzzle1]))
        self.add_quiz(Quiz("Joululauluvisa", [puzzle2]))


    def find_quiz_names(self):
        return self._quiz_repository.find_quiz_names()


    def find_all_quizzes(self):
        return self._quiz_repository.find_all_quizzes()


    def find_quiz(self, name):
        return self._quiz_repository.find_quiz(name)


management_service = ManagementService()
