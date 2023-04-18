from tkinter import ttk, Label, constants

class GameView:

    def __init__(self, root, handle_opening_view):
        self._root = root
        self._handle_opening_view = handle_opening_view
        self._frame = None
        
        self._initialize()
    
    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack()
            
    def _initialize(self):
        self._frame = ttk.Frame(master=self._frame)

        for i in range(1, 6):
            label = Label(master=self._frame,
                height= 2,
                width=6,
                text=str(i),
                font=("Helvetica", 25),
                foreground="white",
                background="blue")
            label.grid(row=0, column=i-1, padx=15, pady=15)

        quit_button = ttk.Button(
            master=self._frame,
            text="Quit",
            command=self._quit_game
        )

        quit_button.grid(row=1, column=0, pady=20)
    
    def _quit_game(self):
        self._handle_opening_view()