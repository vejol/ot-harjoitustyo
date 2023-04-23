from initialize_database import initialize_database
from database_connection import get_database_connection


def build():
    initialize_database()
    
    connection = get_database_connection()
    insert_sample_quizz(connection)
    

def insert_sample_quizz(connection):
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO Quizzes (name) VALUES ('Suomivisa');
    ''')

    cursor.execute('''
        INSERT INTO Puzzles (name, order_no, quizz_id, word1, word2, word3, word4, word5)
            VALUES ('Maamme-laulu (säv. F. Pacius)', 1, 1, 'laaksoa,', 'ei', 'kukkulaa,', 'ei', 'vettä');
    ''')

    connection.commit()


if __name__ == "__main__":
    build()
