from tkinter import ttk, Label, LEFT


class StartView:

    def __init__(self, root, hande_game_view, handle_new_quiz_view):
        self._root = root
        self._frame = None
        self._current_view = None
        self._initialize()

    def pack(self):
        for label in self._labels:
            label.pack(side=LEFT,
                       padx=15)
            
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
