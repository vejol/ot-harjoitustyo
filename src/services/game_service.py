
class GameService:

    def __init__(self, quiz):
        self._quiz = quiz
        self._current_puzzle = self._quiz.puzzles[0]
        self.team1_points = 0
        self.team2_points = 0
        self._puzzle_counter = 0
        self._revealed = [False] * 5

    def add_point_team1(self):
        self.team1_points += 1

    def add_point_team2(self):
        self.team2_points += 1

    def reveal_field(self, n):
        self._revealed[n] = True
        return self._current_puzzle.words[n]
