from random import sample

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
        self._revealed = [False] * 5
        self._red_words = []
        self._initialize_puzzle()

    def _initialize_puzzle(self):
        self._current_puzzle = self._quiz.puzzles.pop(0)
        self._red_words = sample([0, 1, 2, 3, 4], 2)

    def next_puzzle(self):
        self._initialize_puzzle()

    def puzzles_left(self):
        return len(self._quiz.puzzles) > 0

    def add_point(self, team):
        self._points[team] += 1
        return self._points[team]

    def dec_point(self, team):
        self._points[team] -= 1
        return self._points[team]

    def get_answer(self):
        return self._current_puzzle.name

    def get_points(self, team):
        return self._points[team]

    def red_word(self, index):
        """Kertoo, onko kyseisen indeksin sana punainen.

        Args:
            index : Kokonaisluku, joka kuvaa halutun sanan indeksiä.

        Returns:
            Totuusarvo, joka kuvaa, onko kysytyn indeksin sana punainen.
        """

        return index in self._red_words

    def reveal_field(self, index):
        """Paljastaa valitun sanan.

        Args:
            index: Kokonaisluku, joka kuvaa paljastettavan sanan indeksiä.

        Returns:
            Merkkijono, joka kertoo paljastuneen sanan.
        """

        self._revealed[index] = True
        return self._current_puzzle.words[index]
