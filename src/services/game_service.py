from random import sample
from config import RED_WORDS_COUNT


class GameService:
    """Luokka, joka vastaa pelilogiikasta."""

    def __init__(self, quiz):
        """Luokan konstruktori. Luo uuden pelilogiikasta vastaavan palvelun.

        Args:
            quiz: Quiz-olio, joka sisältää pelattavan visailun.
        """

        self._quiz = quiz
        self._current_puzzle = None
        self._points = {"team1": 0, "team2": 0}
        self._red_words = []
        self._initialize_puzzle()

    def add_point(self, team):
        """Lisää pisteen annetulle joukkueelle.

        Args:
            team: Merkkijono, joka kuvaa joukkueen nimeä.

        Returns:
            Kokonaisluku, joka kuvaa joukkueen uutta pistetilannetta.
        """
        self._points[team] += 1
        return self._points[team]

    def dec_point(self, team):
        """Vähentää pisteen annetulta joukkueelta.

        Args:
            team: Merkkijono, joka kuvaa joukkueen nimeä.

        Returns:
            Kokonaisluku, joka kuvaa joukkueen uutta pistetilannetta.
        """
        self._points[team] -= 1
        return self._points[team]

    def get_answer(self):
        """Palauttaa arvoituksen vastauksen.

        Returns:
            Merkkijono, joka kuvaa arvoituksen oikeaa vastausta.
        """
        return self._current_puzzle.name

    def get_points(self, team):
        """Palauttaa annetun tiimin pisteet.

        Args:
            team: halutun tiimin nimi merkkijonona, joko "team1" tai "team2"

        Returns:
            Kokonaisluku, joka kuvaa joukkueen pisteitä.
        """
        return self._points[team]

    def get_word(self, index):
        """Paljastaa valitun sanan.

        Args:
            index: Kokonaisluku, joka kuvaa paljastettavan sanan indeksiä.

        Returns:
            Merkkijono, joka kertoo paljastuneen sanan.
        """

        return self._current_puzzle.words[index]

    def next_puzzle(self):
        """Siirtää ohjelman tilan seuraavaksi vuorossa olevaan arvoitukseen.
        """
        self._initialize_puzzle()

    def puzzles_available(self):
        """Kertoo, onko arvoituksia vielä jäljellä.

        Returns:
            Totuusarvo, joka kuvaa, onko arvoituksia vielä jäljellä
        """
        return len(self._quiz.puzzles) > 0

    def red_word(self, index):
        """Kertoo, onko kyseisen indeksin sana punainen.

        Args:
            index : Kokonaisluku, joka kuvaa halutun sanan indeksiä.

        Returns:
            Totuusarvo, joka kuvaa, onko kysytyn indeksin sana punainen.
        """

        return index in self._red_words

    def _initialize_puzzle(self):
        self._current_puzzle = self._quiz.puzzles.pop(0)
        self._red_words = sample([0, 1, 2, 3, 4], RED_WORDS_COUNT)
