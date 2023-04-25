from services.game_service import GameService
from tkinter import ttk, Label


class GameView:

    def __init__(self, root, handle_opening_view, game_service: GameService):
        self._root = root
        self._handle_opening_view = handle_opening_view
        self._game_service = game_service
        self._frame = None
        self._quiz_fields = []

        self._initialize()
    
    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack()
            
    def _initialize(self):
        self._frame = ttk.Frame(master=self._frame)
        self._initialize_quiz_fields()
        self._pack_quiz_fields()

        quit_button = ttk.Button(
            master=self._frame,
            text="Lopeta",
            command=self._quit_game
        )

        quit_button.grid(row=1, column=0, pady=20)

    def _pack_quiz_fields(self):
        for i in range(len(self._quiz_fields)):
            self._quiz_fields[i].grid(row=0, column=i, padx=15, pady=15)

    def _initialize_quiz_fields(self):
        for i in range(1, 6):
            label = Label(master=self._frame,
                height= 4,
                width=12,
                text=str(i),
                font=("Helvetica", 12),
                foreground="white",
                background="blue")
            label.bind("<Button-1>", lambda event, n=i-1: self._reveal(n))
            self._quiz_fields.append(label)

    
    def _quit_game(self):
        self._handle_opening_view()


    def _reveal(self, n: int):
        word = self._game_service.reveal_field(n)
        self._quiz_fields[n].config(text=word)
