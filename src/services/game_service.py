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
        self._puzzle_counter = 0
        self._revealed = [False] * 5
        self._red_words = []
        self.__initialize_puzzle(0)

    def __initialize_puzzle(self, index):
        self._puzzle_counter += 1
        self._current_puzzle = self._quiz.puzzles[index]
        self._red_words = sample([0, 1, 2, 3, 4], 2)

    def change_points(self, team, amount):
        self._points[team] += amount
        return self._points[team]

    def get_points(self, team):
        return self._points[team]

    def is_red_word(self, index):
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
