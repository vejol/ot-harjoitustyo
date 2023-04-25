from initialize_database import get_database_connection
from entities.quiz import Quiz
from entities.puzzle import Puzzle

class QuizRepository:

    def __init__(self):
        self._connection = get_database_connection()

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute(
            "DELETE FROM Quizzes"
        )

        cursor.execute(
            "DELETE FROM Puzzles"
        )

    def find_all_names(self):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT name FROM Quizzes"
        )

        rows = cursor.fetchall()

        return [row["name"] for row in rows]

    def find_quiz(self, name):

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


    def save(self, quiz: Quiz):
        cursor = self._connection.cursor()

        cursor.execute(
            "INSERT INTO Quizzes (name) VALUES (?)",
            [quiz.name]
        )

        for count, puzzle in enumerate(quiz.puzzles):
            cursor.execute(
                '''INSERT INTO Puzzles (name, 
                                        order_no, 
                                        quiz_id, 
                                        word1, 
                                        word2, 
                                        word3, 
                                        word4, 
                                        word5) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                [puzzle.name,
                 count + 1,
                 cursor.lastrowid,
                 puzzle.words[0],
                 puzzle.words[1],
                 puzzle.words[2],
                 puzzle.words[3],
                 puzzle.words[4]]
            )
