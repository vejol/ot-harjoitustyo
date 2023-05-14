from tkinter import ttk, constants, Frame, messagebox, Toplevel, INSERT
from services.edit_service import (
    EditService,
    MultipleWordsError,
    NoPuzzleNameError,
    NoPuzzlesError,
    NoPuzzleWordError,
    NoQuizNameError,
    PuzzleNameLenghtError,
    PuzzleWordLenghtError,
    QuizExistError
)

class EditView:
    """Luokka, joka vastaa visailujen luomiseen tarkoitetusta näkymästä."""

    def __init__(self, root, handle_opening_view, service: EditService):
        """Luokan konstruktori. Luo uuden visailujenluomisnäkymän.

        Args:
            root: TKinter-elementti, joka sisältää ohjelman ikkunan.
            handle_opening_view: Arvo, jota kutsumalla pääsee takaisin aloitusnäkymään.
            service: EditService-olio, joka vastaa visailujen muokkaamisen ja luomisen logiikasta.
        """

        self._root = root
        self._handle_opening_view = handle_opening_view
        self._service = service

        self._frame = None
        self._puzzle_list_frame = None
        self._puzzle_list_view = None
        self._name_entry = None

        self._initialize()

    def destroy(self):
        """Sulkee näkymän."""
        self._frame.destroy()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)
    
    def _handle_save_and_return(self):
        name = self._name_entry.get()
        name_set = self._try_to_set_quiz_name(name)

        if not name_set:
            return
        
        quiz_saved = self._try_to_save_quiz()

        if quiz_saved:
            self._handle_opening_view()
                
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._puzzle_list_frame = ttk.Frame(master=self._frame)

        self._init_header()
        self._init_puzzle_list()
        self._init_footer()

        self._puzzle_list_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

    def _init_footer(self):

        cancel_button = ttk.Button(
            master=self._frame,
            text="Peruuta",
            command=self._handle_opening_view
        )

        save_button = ttk.Button(
            master=self._frame,
            text="Tallenna",
            command=self._handle_save_and_return
        )

        add_button = ttk.Button(
            master=self._frame,
            text="Lisää arvoitus",
            command=lambda: PuzzleCreationWindow(self._root, self._service, self._init_puzzle_list)
        )

        add_button.grid(row=3, column=0, padx=10, pady=10, sticky=constants.W)
        cancel_button.grid(row=4, column=0, padx=10, pady=10)
        save_button.grid(row=4, column=1, padx=10, pady=10)

    def _init_header(self):
        header_frame = ttk.Frame(master=self._frame)

        quiz_name_label = ttk.Label(
            master=header_frame,
            text="Visailun nimi:",
            font="Helvetica 10 bold"
        )
        
        self._name_entry = ttk.Entry(master=header_frame)
        self._set_default_name()

        quiz_name_label.grid(row=0, column=0, padx=10, pady=20)
        self._name_entry.grid(row=0, column=1, padx=10, pady=20, sticky=constants.EW)
        header_frame.grid(row=0, column=0, columnspan=2, sticky=constants.EW)
        header_frame.grid_columnconfigure(1, weight=1)

    def _init_puzzle_list(self):
        if self._puzzle_list_view:
            self._puzzle_list_view.destroy()

        puzzles = self._service.get_puzzles()
        self._puzzle_list_view = PuzzleListView(
            self._puzzle_list_frame, 
            self._service,
            puzzles,
            self._init_puzzle_list
        )

        self._puzzle_list_view.pack()

    def _set_default_name(self):
        quiz_name = self._service.get_name()
        self._name_entry.insert(INSERT, quiz_name)
    
    def _try_to_save_quiz(self):
        try:
            self._service.save_quiz()
            return True

        except NoPuzzlesError:
            messagebox.showinfo(
                title="Ei arvoituksia",
                message="Lisää vähintään yksi arvoitus, jotta voit tallentaa visailun."
            )

    def _try_to_set_quiz_name(self, name):
        try:
            self._service.set_name(name)
            return True

        except NoQuizNameError:
            messagebox.showinfo(
                title="Visailun nimi puuttuu", 
                message="Anna ensin visailulle jokin nimi!"
            )

        except QuizExistError:
            messagebox.showinfo(
                title="Virheellinen nimi", 
                message="Saman niminen visailu on jo olemassa, valitse jokin toinen nimi."
            )



class PuzzleListView:
    """Arvoitusten listaamisesta vastaava näkymä."""
     
    def __init__(self, root, service, puzzles, handle_update_list_view):
        """Luokan konstruktori. Luo uuden arvoituksia listaavan näkymän.

        Args:
            root: TKinter-elementti, joka sisältää ohjelman ikkunan.
            service: EditService-olio, joka vastaa visailujen muokkaamisen ja luomisen logiikasta.
            puzzles: Lista, joka sisältää näkymään lisättävät arvoitukset.
            handle_update_list_view: Arvo, jota kutsumalla visailulistaus päivittyy.
        """

        self._root = root
        self._service = service
        self._puzzles = puzzles
        self._handle_update_list_view = handle_update_list_view
        self._frame = None

        self._initialize()
    
    def destroy(self):
        """Sulkee näkymän."""
        self._frame.destroy()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X, padx=20, pady=20)

    def _handle_remove(self, n):
        self._service.remove_puzzle(n)
        self._handle_update_list_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for n, puzzle in enumerate(self._puzzles):
            self._init_puzzle_frame(puzzle.name, puzzle.words, n)
    
    def _init_puzzle_frame(self, name, words, n):
        puzzle_frame = Frame(
            master=self._frame,
            highlightbackground="grey",
            highlightthickness=2)
        
        puzzle_label = ttk.Label(
            master=puzzle_frame, 
            text=f"Arvoitus {n+1}",
            font="Helvetica 10 bold"
        )

        name_label = ttk.Label(
            master=puzzle_frame, 
            text=f"Kappaleen nimi: {name}"
        )

        words_label = ttk.Label(
            master=puzzle_frame,
            text=f"Piilotettavat sanat: {words}"
        )

        remove_button = ttk.Button(
            master=puzzle_frame,
            text="Poista",
            command=lambda: self._handle_remove(n)
        )
        
        puzzle_label.grid(row=0, column=0, padx=10, pady=10, sticky=constants.W)
        remove_button.grid(row=0, column=1, padx=10, pady=10, sticky=constants.E)
        name_label.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky=constants.EW)
        words_label.grid(row=2, column=0, padx=10, pady=0, columnspan=2, sticky=constants.EW)

        puzzle_frame.grid_columnconfigure(0, weight=1)
        puzzle_frame.pack(fill=constants.X)



class PuzzleCreationWindow:
    """Uuden arvoituksen luomisesta vastaava ikkuna.
    """

    def __init__(self, root, edit_service, handle_update):
        """Luokan konstruktori. Luo uuden arvoitusten luomisesta vastaavan ikkunan.

        Args:
            root: TKinter-elementti, joka sisältää ohjelman aiemman ikkunan.
            edit_service: EditService-olio, joka vastaa visailujen muokkaamisen ja luomisen logiikasta.
            handle_update: Arvo, jota kutsumalla voi päivittää alemman ikkunan arvoituslistauksen.
        """
        self._root = root
        self._service = edit_service
        self._handle_update = handle_update

        self._window = None
        self._frame = None

        self._init_window()
        self._initialize()

    def _get_inserted_text(self):
        input = []
        input_frame = self._frame.winfo_children()[0]
        info_frame_widgets = input_frame.winfo_children()

        for widget in info_frame_widgets:
            if widget.winfo_class() == "TEntry":
                input.append(widget.get())

        return input

    def _initialize(self):
        self._frame = ttk.Frame(master=self._window)

        self._init_input_frame()
        self._init_footer()
        
        self._frame.pack(fill=constants.X, padx=10, pady=10)

    def _init_footer(self):
        cancel_button = ttk.Button(
            master=self._frame,
            text="Peruuta",
            command=self._window.destroy
        )

        add_button = ttk.Button(
            master=self._frame,
            text="Tallenna",
            command=self._handle_save_changes
        )

        cancel_button.grid(row=1, column=0, padx=30, pady=10, sticky=constants.E)
        add_button.grid(row=1, column=1, padx=30, pady=10, sticky=constants.W)
    
    def _init_input_frame(self):
        input_frame = Frame(master=self._frame)

        name_label = ttk.Label(
            master=input_frame, 
            text="Kappaleen nimi: "
        )

        name_entry = ttk.Entry(
            master=input_frame
        )

        words_label = ttk.Label(
            master=input_frame,
            text="Piilotettavat sanat: "
        )

        self._init_puzzle_word_entries(input_frame, 5)
        
        name_label.grid(row=0, column=0, columnspan=3, padx=5, pady=(10,0), sticky=constants.W)
        name_entry.grid(row=1, column=0, columnspan=5, padx=5, pady=5, sticky=constants.EW)
        words_label.grid(row=2, column=0, columnspan=3, padx=5, pady=(10,5), sticky=constants.W)
        input_frame.grid(row=0, column=0, columnspan=2)

    def _init_puzzle_word_entries(self, frame, count):
        for i in range(count):

            entry = ttk.Entry(
                master=frame, 
                width=10
            )
            
            label = ttk.Label(
                master=frame, 
                text=f"sana{i+1}", 
                font="Helvetica 8 italic"
            )
            
            entry.grid(row=3, column=i, padx=5, pady=0)
            label.grid(row=4, column=i, padx=5, pady=5)

    def _init_window(self):
        self._window = Toplevel(self._root)
        self._window.grab_set()
        self._window.title("Lisää uusi arvoitus")
    
    def _handle_save_changes(self):
        user_input = self._get_inserted_text()
        name  = user_input[0]
        words = user_input[1:]

        succeed = self._try_to_add_puzzle(name, words)
 
        if succeed:        
            self._handle_update()
            self._window.destroy()
    
    def _try_to_add_puzzle(self, name, words):
        try:
            self._service.add_puzzle(name, words)
            return True

        except NoPuzzleNameError:
            messagebox.showinfo(
                title="Nimi puuttuu", 
                message="Anna arvoitukselle ensin jokin nimi!"
            )
        
        except PuzzleNameLenghtError:
            messagebox.showinfo(
                title="Liian pitkä nimi", 
                message="Syötetty nimi on liian pitkä. Anna nimi, jonka pituus on enintään 100 merkkiä."
            )

        except NoPuzzleWordError:
            messagebox.showinfo(
                title="Piilotettava sana puuttuu", 
                message="Yksi tai useampi piilotettava sana puuttuu. Syötä ensin sana jokaiseen sanakenttään."
            )

        except MultipleWordsError:
            messagebox.showinfo(
                title="Useita sanoja sanakentässä", 
                message="Syötä vain yksi sana kuhunkin sanakenttään. Älä käytä välilyöntejä."
            )
    
        except PuzzleWordLenghtError:
            messagebox.showinfo(
                title="Liian pitkä sana", 
                message="Yksi tai useampi piilotettava sana on liian pitkä. Varmista, että kunkin sanan pituus on enintään 12 merkkiä."
            )
