from entities.quiz import Quiz
from entities.puzzle import Puzzle
from initialize_database import get_database_connection

class QuizRepository:
    """Luokka, joka vastaa visailuihin liittyvistä tietokantaoperaatioista."""

    def __init__(self):
        """Luokan konstruktori. Luo uuden tietokantaoperaatioista vastaavan olion."""
        self._connection = get_database_connection()

    def delete_all(self):
        """Tyhjentää kaikki tietokantataulut."""
        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM Quizzes"
        )

        cursor.execute(
            "DELETE FROM Puzzles"
        )

    def delete_quiz(self, quiz):
        """Poistaa tietokannasta annetun visailun tiedot.

        Args:
            quiz (Quiz): Quiz-olio, joka kuvaa poistettavaa oliota.
        """
        cursor = self._connection.cursor()

        cursor.execute("SELECT id FROM Quizzes WHERE name=?", [quiz.name])
        quiz_id = cursor.fetchall()[0][0]

        cursor.execute("DELETE FROM Quizzes WHERE (name=?)", [quiz.name])
        cursor.execute("DELETE FROM Puzzles WHERE (quiz_id=?)", [quiz_id])

        self._connection.commit()

    def find_all_quizzes(self):
        """Palauttaa kaikki tietokantaan tallennetut visailut.

        Returns:
            Sanakirja, jonka avaimena on visailun nimi ja arvona 
            nimeä vastaava Quiz-olio.
        """

        quiz_names = self.find_quiz_names()

        quizzes = {}
        for name in quiz_names:
            quizzes[name] = self.find_quiz(name)

        return quizzes


    def find_quiz_names(self):
        """Hakee tietokannasta kaikkien visailujen nimet.

        Returns:
            Lista, joka sisältää kaikkien tietokannassa olevien
            visailujen nimet.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT name FROM Quizzes"
        )

        rows = cursor.fetchall()
        return [row["name"] for row in rows]


    def find_quiz(self, name):
        """Hakee tietokannasta visailun nimen perusteella.

        Args:
            name: Merkkijono, joka kuvaa visailun nimeä.

        Returns:
            Quiz-olio, joka vastaa parametriksi annettua nimeä.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM Puzzles P, Quizzes Q WHERE Q.name=? AND Q.id=P.quiz_id",
            [name]
        )

        puzzle_data = cursor.fetchall()

        puzzles = []
        for row in puzzle_data:
            puzzle_name = row["name"]
            words = [row["word1"],
                    row["word2"],
                    row["word3"],
                    row["word4"],
                    row["word5"]]
            order_no = row["order_no"]
            puzzles.append(Puzzle(puzzle_name, words, order_no))

        return Quiz(name, puzzles)


    def save_quiz(self, quiz):
        """Tallentaa annetun visailun tietokantaan.

        Args:
            quiz: Olio, joka kuvaa tallennettavaa visailua.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO Quizzes (name) VALUES (?)",
            [quiz.name]
        )

        quiz_id = cursor.lastrowid
        self._save_puzzles(quiz.puzzles, quiz_id, cursor)

        self._connection.commit()

    def update_quiz(self, updated_quiz, old_name):
        """Päivittää annetun visailun tiedot tietokantaan.

        Args:
            updated_quiz: Päivitetty visailu Quiz-oliona.
            old_name: Merkkijono, joka kuvaa visailun aiempaa nimeä.
                      Tämän perusteella visailu on mahdollista löytää tietokannasta.
        """

        cursor = self._connection.cursor()

        quiz_id = self._get_quiz_id(old_name, cursor)
        self._update_quiz_name(updated_quiz.name, quiz_id)
        self._delete_puzzles_by_quiz_id(quiz_id, cursor)
        self._save_puzzles(updated_quiz.puzzles, quiz_id, cursor)

        self._connection.commit()

    def _delete_puzzles_by_quiz_id(self, quiz_id, cursor):
        cursor.execute("DELETE FROM Puzzles WHERE (quiz_id=?)", [quiz_id])

    def _get_quiz_id(self, quiz_name, cursor):
        cursor.execute(
            "SELECT id FROM Quizzes WHERE name=?",
            [quiz_name]
        )

        quiz_id = cursor.fetchall()[0]["id"]
        return quiz_id

    def _save_puzzles(self, puzzles, quiz_id, cursor):
        for order_no, puzzle in enumerate(puzzles):
            cursor.execute(
                '''INSERT INTO Puzzles (
                        name, 
                        order_no, 
                        quiz_id, 
                        word1, 
                        word2, 
                        word3, 
                        word4, 
                        word5)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                [puzzle.name,
                    order_no,
                    quiz_id,
                    puzzle.words[0],
                    puzzle.words[1],
                    puzzle.words[2],
                    puzzle.words[3],
                    puzzle.words[4]]
            )

    def _update_quiz_name(self, name, quiz_id):
        cursor = self._connection.cursor()

        cursor.execute(
            "UPDATE Quizzes SET name=? WHERE id=?",
            [name,
             quiz_id]
        )
