from ui.game_view import GameView
from ui.start_view import StartView


class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_start_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_create_quiz_view(self):
        return

    def _show_game_view(self):
        self._current_view = GameView(self._root)
        self._current_view.pack()

    def _show_start_view(self):
        self._hide_current_view()

        self._current_view = StartView(
            self._root,
            self._show_game_view,
            self._show_create_quiz_view)

        self._current_view.pack()
