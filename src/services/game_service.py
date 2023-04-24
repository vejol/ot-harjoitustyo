#from entities.quiz import Quiz

class GameService:

    def __init__(self, quiz):
        self.quiz = quiz
        self.turn = 1
        self.team1_points = 0
        self.team2_points = 0
        self._puzzle_counter = 0

    def add_point_team1(self):
        self.team1_points += 1

    def add_point_team2(self):
        self.team2_points += 1

    def change_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def _reveal_field(self):
        return
