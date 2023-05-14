from entities.puzzle import Puzzle
from entities.quiz import Quiz
from repositories.quiz_repository import QuizRepository

class ManagementService:
    """Luokka, joka vastaa sovelluksen logiikasta."""

    def __init__(self, repository):
        """Luokan konstruktori. Luo uuden sovelluksen logiikasta vastaavan palvelun."""
        self._repository = repository


    def add_quiz(self, quiz):
        """Lisää uuden visailun

        Args:
            quiz: Lisättävä Quiz-olio.
        """

        self._repository.save_quiz(quiz)

    def delete_quiz(self, quiz_name):
        self._repository.delete_quiz(quiz_name)


    def add_default_quizzes(self):
        """Lisää sovellukseen mallivisailut."""

        puzzle1 = Puzzle("Maamme-laulu", ["laaksoa", "ei", "kukkulaa", "ei", "vettä"], 1)
        puzzle2 = Puzzle("Kalliolle kukkulalle",
                         ["kalliolle", "kukkulalle", "rakennan", "minä", "majani"], 2)
        puzzle3 = Puzzle("Petteri Punakuono", ["pitkä", "on", "taival", "valoton,", "Petteri"], 1)

        self.add_quiz(Quiz("Suomivisa", [puzzle1, puzzle2]))
        self.add_quiz(Quiz("Joululauluvisa", [puzzle3]))


    def get_quiz_names(self):
        """Palauttaa tallennettujen visailujen nimet.

        Returns:
            Lista, joka sisältää tallennettujen visailujen nimet.
        """

        return self._repository.find_quiz_names()


    def find_all_quizzes(self):
        """Palauttaa kaikki tallennetut visailut.

        Returns:
            Lista, joka sisältää kaikki ohjelmaan tallennetut visailut Quiz-olioina.
        """
        return self._repository.find_all_quizzes()


    def get_quiz(self, name):
        """Palauttaa halutun visailun nimen perusteella.

        Args:
            name: Halutun visailun nimi merkkijonona.

        Returns:
            Quiz-olio, joka vastaa parametriksi annettua visailun nimeä.
        """

        return self._repository.find_quiz(name)
