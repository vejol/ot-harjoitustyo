from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa olemassa olevat tietokantataulut.

    Args:
        connection: Connection-olio, jolla hallitaan tietokantayhteyttä.
    """

    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS Quizzes;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS Puzzles;
    ''')

    connection.commit()


def create_tables(connection):
    """Luo ohjelman suoritukseen tarvittavat tietokantataulut.

    Args:
        connection: Connection-olio, jolla hallitaan tietokantayhteyttä.
    """

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
    """Alustaa tarvittavat tietokantataulut."""

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

    connection.commit()


if __name__ == "__main__":
    initialize_database()
    