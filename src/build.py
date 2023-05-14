from initialize_database import initialize_database
from services.management_service import ManagementService
from repositories.quiz_repository import QuizRepository

def build():
    initialize_database()
    service = ManagementService(QuizRepository())
    service.add_default_quizzes()


if __name__ == "__main__":
    build()
