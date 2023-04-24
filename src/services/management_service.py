from repositories.quiz_repository import QuizRepository

class ManagementService:

    def __init__(self):
        self._quiz_repository = QuizRepository()

    def get_quiz_names(self):
        return self._quiz_repository.find_all_names()

    def find_quiz(self, name):
        return self._quiz_repository.find_quiz(name)


management_service = ManagementService()
