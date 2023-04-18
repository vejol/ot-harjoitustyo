from tkinter import ttk, constants


class OpeningView:

    def __init__(self, root, hande_game_view, handle_new_quiz_view):
        self._root = root
        self._handle_game_view = hande_game_view
        self._handle_new_quiz_view = handle_new_quiz_view
        self._frame = None

        self._initialize()
    
    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)
            
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        start_game_button = ttk.Button(
            master=self._frame,
            text="Start Game",
            command=self._handle_game_view
        )

        create_quiz_button = ttk.Button(
            master=self._frame,
            text="Create New Quiz",
            command=self._handle_new_quiz_view
        )

        welcome_label = ttk.Label(
            master=self._frame, 
            text="Welcome to Bumtsibum!",
            font=("Helvetica", 25)
        )
        
        welcome_label.grid(row=0, column=0, columnspan=2)
        start_game_button.grid(row=1, column=0)
        create_quiz_button.grid(row=1, column=1)


