from initialize_database import initialize_database
from services.management_service import management_service

def build():
    initialize_database()
    management_service.add_default_quizzes()


if __name__ == "__main__":
    build()
