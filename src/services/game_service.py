class GameService:

    def __init__(self):
        self.turn = 1
        self.__team1_points = 0
        self.__team2_points = 0

    def add_point_team1(self):
        self.__team1_points += 1
    
    def add_point_team2(self):
        self.__team2_points += 1

    def change_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    