from tkinter import ttk, Label, Frame, constants
from PIL import Image, ImageTk
import os

class GameView:
    """Luokka, joka vastaa pelinäkymästä."""

    def __init__(self, root, handle_opening_view, game_service):
        """Luokan konstruktori. Luo uuden pelinäkymän.

        Args:
            root: TKinter-elementti, joka sisältää ohjelman ikkunan.
            handle_opening_view: Arvo, jota kutsumalla pääsee takaisin aloitusnäkymään.
            game_service: Olio, joka vastaa pelin logiikasta.
        """

        self._root = root
        self._handle_opening_view = handle_opening_view
        self._game_service = game_service

        self._frame = None
        self._blue_field_img = None
        self._red_field_img = None
        self._team1_points_label = None
        self._team2_points_label = None
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

    def _initialize(self):
        self._frame = Frame(master=self._frame, bg="#1E3E5D")
        self._initialize_images()

        self._initialize_quiz_fields()
        self._pack_quiz_fields()

        self._init_point_counter("team1")
        #self._init_point_counter("team2")

        quit_button = ttk.Button(
            master=self._frame,
            text="Lopeta",
            command=self._handle_quit_game
        )

        self._root.grid_columnconfigure(0, weight=1)
        quit_button.grid(row=2, column=0, pady=20)

    def _initialize_images(self):
        current_path = os.path.dirname(__file__)
        img_path = os.path.join(current_path, "..", "..", "img")
        self._blue_field_img = self._init_field_img(os.path.join(img_path, "blue.png"))
        self._red_field_img = self._init_field_img(os.path.join(img_path, "red.png"))

    def _init_field_img(self, dirname):
        img = Image.open(dirname)
        img_size = self._root.winfo_screenwidth() // 6
        resized_img = img.resize((img_size, img_size))
        return ImageTk.PhotoImage(resized_img)

    def _pack_quiz_fields(self):
        for i in range(len(self._quiz_fields)):
            pad_size = self._root.winfo_screenwidth() // 60
            self._quiz_fields[i].grid(row=0, column=i, padx=pad_size, pady=pad_size)
    
    def _init_point_counter(self, team):
        points_frame = Frame(master=self._frame, bg="#1E3E5D")

        team_name_label = Label(master=points_frame,
            text="Joukkue 1:n\npisteet",
            font=("Calibri", 26),
            fg="#FFFFFF",
            bg="#1E3E5D"
            )

        dec_point_team1_button = ttk.Button(
            master=points_frame,
            text="-",
            command=lambda: self._change_points(team, -1)
        )

        self._add_point_team1_button = ttk.Button(
            master=points_frame,
            text="+",
            command=lambda: self._change_points(team, 1)
        )

        team1_points_label = Label(master=points_frame,
            text=self._game_service.get_points(team),
            font=("Calibri", 26),
            fg="#FFFFFF",
            bg="#1E3E5D"
            )

        team_name_label.grid(row=0,column=0,columnspan=3)
        dec_point_team1_button.grid(row=1, column=0, pady=20)
        team1_points_label.grid(row=1, column=1, padx=20, pady=20)
        self._add_point_team1_button.grid(row=1, column=2, pady=20)
        points_frame.grid(row=1, column=0, columnspan=2, padx=100, pady=100)

    def _change_points(self, team, amount):
        points = self._game_service.change_points(team, amount)
        self._team1_points_label.config(text=points)

    def _initialize_quiz_fields(self):

        for i in range(1, 6):
            label = Label(master=self._frame,
                text=str(i),
                font=("Calibri", 26),
                fg="#FFFFFF",
                bg="#1E3E5D",
                image=self._blue_field_img,
                compound="center"
                )
            label.bind("<Button-1>", lambda event, n=i-1: self._handle_reveal_word(n))
            self._quiz_fields.append(label)

    
    def _handle_quit_game(self):
        self._handle_opening_view()


    def _handle_reveal_word(self, n: int):
        word = self._game_service.reveal_field(n)
        self._quiz_fields[n].config(text=word)
        if self._game_service.is_red_word(n):
            self._quiz_fields[n].config(image=self._red_field_img)
