from tkinter import ttk, constants, Listbox, messagebox, constants
from services.management_service import management_service


class OpeningView:
    """Luokka, joka vastaa ohjelman käyttöliittymän aloitusnäkymästä."""

    def __init__(self, root, hande_game_view, handle_new_quiz_view):
        """Luokan konstruktori. Luo uuden aloitusnäkymän.

        Args:
            root: TKinter-elementti, joka sisältää ohjelman ikkunan.
            hande_game_view: Arvo, jota kutsumalla avautuu uusi pelinäkymä.
            handle_new_quiz_view: Arvo, jota kutsumalla avautuu uusi visailujenluomisnäkymä.
        """

        self._root = root
        self._handle_game_view = hande_game_view
        self._handle_new_quiz_view = handle_new_quiz_view
        self._quiz_list = None
        self._frame = None

        self._initialize()
    
    def destroy(self):
        """Sulkee näkymän."""
        self._frame.destroy()

    def _get_selected_quiz_name(self):
        value = self._quiz_list.curselection()

        if not value:
            return None
        
        return self._quiz_list.get(value)

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X, padx=10, pady=10)
            
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._init_header()        
        self._init_quiz_list()
        self._init_left_panel()
        self._init_footer()

    def _init_footer(self):
        start_game_button = ttk.Button(
            master=self._frame,
            text="Aloita peli",
            command=lambda: self.__take_action(self._handle_game_view)
        )

        start_game_button.grid(
            row=5, 
            column=0,
            columnspan=2,
            padx=10, 
            pady=20
        )

    def _init_left_panel(self):
        create_quiz_button = ttk.Button(
            master=self._frame,
            text="Luo uusi peli",
            command=self._handle_new_quiz_view
        )

        modify_button = ttk.Button(
            master=self._frame,
            text="Muokkaa",
            command=lambda: self.__take_action(self._handle_new_quiz_view)
        )

        delete_button = ttk.Button(
            master=self._frame,
            text="Poista",
            command=""
        )

        create_quiz_button.grid(
            row=1, 
            column=1, 
            padx=10, 
            pady=(20, 0), 
            sticky=constants.N
        )

        modify_button.grid(
            row=2, 
            column=1, 
            padx=10, 
            pady=0, 
            sticky=constants.N
        )

        delete_button.grid(
            row=3, 
            column=1, 
            padx=10, 
            pady=0, 
            sticky=constants.N
        )

    def _init_header(self):
        quiz_label = ttk.Label(
            master=self._frame, 
            text="Tallennetut visailut:",
            font=("Helvetica", 12, "bold")
        )

        quiz_label.grid(
            row=0, 
            column=0, 
            sticky=constants.W
        )

    def _init_quiz_list(self):
        self._quiz_list = Listbox(master=self._frame)

        quiz_names = management_service.get_quiz_names()
        for counter, quiz_name in enumerate(quiz_names):
            self._quiz_list.insert(counter, quiz_name)

        self._quiz_list.grid(
            row=1, 
            column=0,
            rowspan=4,
            padx=10,
            pady=10,
            sticky=constants.EW
        )
    
    def _show_quiz_messagebox(self):
        messagebox.showinfo(
            title="Valitse visailu", 
            message="Valitse ensin haluamasi visailu listalta!"
        )

    def __take_action(self, action_handle):
        quiz_name = self._get_selected_quiz_name()

        if not quiz_name:
            self._show_quiz_messagebox()
            return

        selected_quiz = management_service.get_quiz(quiz_name)
        action_handle(selected_quiz)
