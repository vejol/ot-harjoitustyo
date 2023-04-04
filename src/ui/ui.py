from ui.game_view import GameView
class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_game_view()
    
    def _show_game_view(self):
        self._current_view = GameView(self._root)
        self._current_view.pack()