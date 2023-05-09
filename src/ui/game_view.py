from config import BLUE_IMG_FILE_PATH, RED_IMG_FILE_PATH
from services.game_service import GameService
from tkinter import ttk, Label, Frame, constants
from PIL import Image, ImageTk

class GameView:
    """Luokka, joka vastaa pelinäkymästä."""

    def __init__(self, root, handle_opening_view, game_service: GameService):
        """Luokan konstruktori. Luo uuden pelinäkymän.

        Args:
            root: TKinter-elementti, joka sisältää ohjelman ikkunan.
            handle_opening_view: Arvo, jota kutsumalla pääsee takaisin aloitusnäkymään.
            game_service: Olio, joka vastaa pelin logiikasta.
        """

        self._root = root
        self._handle_opening_view = handle_opening_view
        self._service = game_service

        self._frame = None
        self._blue_img = None
        self._red_img = None
        self._quiz_fields = []

        self._initialize()
    
    def destroy(self):
        """Sulkee näkymän."""
        self._frame.destroy()
        self._root.attributes('-fullscreen', False)

    def pack(self):
        """Avaa näkymän."""
        self._frame.pack()
        self._root.attributes('-fullscreen', True)

    def _handle_add_point(self, team, handle_label):
        points = self._service.add_point(team)
        handle_label.config(text=points)

    def _handle_dec_point(self, team, handle_label):
        points = self._service.dec_point(team)
        handle_label.config(text=points)
    
    def _handle_next_puzzle(self):
        if self._service.puzzles_left():
            self._service.next_puzzle()
            self._reset_view()

    def _handle_quit_game(self):
        self._handle_opening_view()

    def _handle_reveal_answer(self):
        answer = self._service.get_answer()
        
        answer_label = Label(master=self._frame,
            text=answer,
            font="Helvetica 24 bold",
            fg="#FFFFFF",
            bg="#1E3E5D"
        )
        
        answer_label.grid(row=4,column=0, columnspan=5)
        self.pack()

    def _handle_reveal_word(self, n: int):
        word = self._service.reveal_field(n)
        self._quiz_fields[n].config(text=word)
        if self._service.red_word(n):
            self._quiz_fields[n].config(image=self._red_img)

    def _initialize(self):
        self._frame = Frame(master=self._root, bg="#1E3E5D")
        self._init_images()

        self._init_quiz_fields()
        self._pack_quiz_fields()

        team1_points_frame = self._init_point_counter("team1", "Joukkue 1:n\npisteet")
        team2_points_frame = self._init_point_counter("team2", "Joukkue 2:n\npisteet")

        team1_points_frame.grid(row=1, column=0, columnspan=2, padx=100, pady=100)
        team2_points_frame.grid(row=1, column=2, columnspan=3, padx=100, pady=100)

        reveal_answer_button = ttk.Button(
            master=self._frame,
            text="Näytä oikea vastaus",
            command=self._handle_reveal_answer
        )

        next_quiz_button = ttk.Button(
            master=self._frame,
            text="Siirry seuraavaan arvoitukseen",
            command=self._handle_next_puzzle
        )

        quit_button = ttk.Button(
            master=self._frame,
            text="Lopeta",
            command=self._handle_quit_game
        )

        self._root.grid_columnconfigure(0, weight=1)
        reveal_answer_button.grid(row=5, column=0)

        if self._service.puzzles_left():
            next_quiz_button.grid(row=5, column=1)

        quit_button.grid(row=5, column=4, pady=20)

    def _init_images(self):
        img = Image.open(BLUE_IMG_FILE_PATH)
        img_size = self._root.winfo_screenwidth() // 6
        resized_img = img.resize((img_size, img_size))
        self._blue_img = ImageTk.PhotoImage(resized_img)

        img = Image.open(RED_IMG_FILE_PATH)
        img_size = self._root.winfo_screenwidth() // 6
        resized_img = img.resize((img_size, img_size))
        self._red_img = ImageTk.PhotoImage(resized_img)
    
    def _init_point_counter(self, team, label_text):
        points_frame = Frame(master=self._frame, bg="#1E3E5D")

        team_name_label = Label(master=points_frame,
            text=label_text,
            font=("Calibri", 26),
            fg="#FFFFFF",
            bg="#1E3E5D"
            )

        points_label = Label(master=points_frame,
            text=self._service.get_points(team),
            font=("Helvetica", 60),
            fg="#FFFFFF",
            bg="#1E3E5D"
            )

        dec_point_button = ttk.Button(
            master=points_frame,
            text="-",
            command=lambda: self._handle_dec_point(team, points_label),
            width=3
        )

        add_point_button = ttk.Button(
            master=points_frame,
            text="+",
            command=lambda: self._handle_add_point(team, points_label),
            width=3
        )

        team_name_label.grid(row=0,column=0,columnspan=3)
        dec_point_button.grid(row=1, column=0, pady=20, sticky=constants.E)
        points_label.grid(row=1, column=1, padx=20, pady=20)
        add_point_button.grid(row=1, column=2, pady=20, sticky=constants.W)

        return points_frame

    def _init_quiz_fields(self):

        for i in range(5):

            label = Label(master=self._frame,
                text=str(i+1),
                font=("Calibri", 26),
                fg="#FFFFFF",
                bg="#1E3E5D",
                image=self._blue_img,
                compound="center"
                )

            label.bind("<Button-1>", lambda event, n=i: self._handle_reveal_word(n))
            self._quiz_fields.append(label)

    def _pack_quiz_fields(self):
        for i in range(len(self._quiz_fields)):
            pad_size = self._root.winfo_screenwidth() // 60
            self._quiz_fields[i].grid(row=0, column=i, padx=pad_size, pady=pad_size)

    def _reset_view(self):
        self._frame.destroy()
        self._quiz_fields = []
        self._initialize()
        self.pack()
