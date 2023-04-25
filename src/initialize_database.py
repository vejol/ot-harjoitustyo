from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS Quizzes;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS Puzzles;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE Quizzes (
            id INTEGER PRIMARY KEY,
            name TEXT
        );
    ''')

    cursor.execute('''
            create table Puzzles (
            id INTEGER PRIMARY KEY,
            name TEXT,
            order_no INTEGER,
            quiz_id INTEGER,
            word1 TEXT,
            word2 TEXT,
            word3 TEXT,
            word4 TEXT,
            word5 TEXT
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    insert_sample_quizzes(connection)


def insert_sample_quizzes(connection):
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO Quizzes (name) VALUES ('Suomivisa');
    ''')

    cursor.execute('''
        INSERT INTO Quizzes (name) VALUES ('Pop-visa');
    ''')

    cursor.execute('''
        INSERT INTO Quizzes (name) VALUES ('Joululauluvisa');
    ''')

    cursor.execute('''
        INSERT INTO Puzzles (name, order_no, quiz_id, word1, word2, word3, word4, word5)
            VALUES ('Maamme-laulu (säv. F. Pacius)', 1, 1, 'laaksoa,', 'ei', 'kukkulaa,', 'ei', 'vettä');
    ''')

    connection.commit()


if __name__ == "__main__":
    initialize_database()
    