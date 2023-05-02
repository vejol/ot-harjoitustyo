class Quiz:
    """Luokka, joka kuvaa visailua."""

    def __init__(self, name: str, puzzles: list):
        """Luokan konstruktori, joka luo uuden visailua kuvaavan olion.

        Args:
            name: Visailun nimeä kuvaava merkkijono.
            puzzles: Lista, joka sisältää visailuun liittyvät arvoitukset Puzzle-olioina.
        """

        self.name = name
        self.puzzles = puzzles
