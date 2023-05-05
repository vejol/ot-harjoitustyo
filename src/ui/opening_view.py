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
        self._frame = None

        self._initialize()
    
    def destroy(self):
        """Sulkee näkymän."""
        self._frame.destroy()

    def __selected_quiz_name(self):
        value = self.__quiz_list.curselection()

        if not value:
            return None
        
        return self.__quiz_list.get(value)


    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X, padx=10, pady=10)
            
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        start_game_button = ttk.Button(
            master=self._frame,
            text="Aloita peli",
            command=lambda: self.__take_action(self._handle_game_view)
        )

        modify_button = ttk.Button(
            master=self._frame,
            text="Muokkaa",
            command=lambda: self.__take_action(self._handle_new_quiz_view)
        )

        create_quiz_button = ttk.Button(
            master=self._frame,
            text="Luo uusi peli",
            command=self._handle_new_quiz_view
        )

        quiz_label = ttk.Label(
            master=self._frame, 
            text="Tallennetut visailut:",
            font=("Helvetica", 12, "bold")
        )
        
        self.__quiz_list = Listbox(
            master=self._frame
        )

        quiz_names = management_service.get_quiz_names()

        for counter, quiz_name in enumerate(quiz_names):
            self.__quiz_list.insert(counter, quiz_name)

        quiz_label.grid(row=0, column=0, columnspan=2, sticky=constants.W)
        self.__quiz_list.grid(row=1, column=0, columnspan=3, sticky=constants.EW)
        start_game_button.grid(row=2, column=0, padx=10, pady=10)
        modify_button.grid(row=2, column=1, padx=10, pady=10)
        create_quiz_button.grid(row=2, column=2, padx=10, pady=10)
    
    def _show_quiz_messagebox(self):
        messagebox.showinfo(
            title="Valitse visailu", 
            message="Valitse ensin haluamasi visailu listalta!"
        )

    def __take_action(self, action_handle):
        quiz_name = self.__selected_quiz_name()

        if not quiz_name:
            self._show_quiz_messagebox()
            return

        selected_quiz = management_service.get_quiz(quiz_name)
        action_handle(selected_quiz)
