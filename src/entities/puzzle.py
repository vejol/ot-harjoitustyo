class Puzzle:

    def __init__(self, name, words, order_no):
        self.name = name
        self.words = [w.upper() for w in words]
        self.order_no = order_no
