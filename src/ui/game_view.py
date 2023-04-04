from tkinter import ttk, Label, LEFT

class GameView:

    def __init__(self, root):
        self._root = root
        self._frame = None
        self._current_view = None
        self._labels = []
        for i in range(1, 6):
            label = Label(self._root,
                height= 2,
                width=6,
                text=str(i),
                font=("Helvetica", 25),
                foreground="white",
                background="blue")
            self._labels.append(label)
        
        self._initialize()

    def pack(self):
        for label in self._labels:
            label.pack(side=LEFT,
                    padx=15)
            
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)