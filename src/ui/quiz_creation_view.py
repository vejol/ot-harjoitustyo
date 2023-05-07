from tkinter import ttk, constants, Frame, Toplevel

class QuizCreationView:
    """Luokka, joka vastaa visailujen luomiseen tarkoitetusta näkymästä."""

    def __init__(self, root, handle_opening_view, quiz):
        """Luokan konstruktori. Luo uuden visailujenluomisnäkymän.

        Args:
            root: TKinter-elementti, joka sisältää ohjelman ikkunan.
            handle_opening_view: Arvo, jota kutsumalla pääsee takaisin aloitusnäkymään.
        """

        self._root = root
        self._handle_opening_view = handle_opening_view
        self._quiz = quiz
        
        self._frame = None
        self._puzzle_query_frame = None
        self._puzzle_query_view = None

        self._initialize()

    def destroy(self):
        """Sulkee näkymän."""
        self._frame.destroy()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)
                
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._puzzle_query_frame = ttk.Frame(master=self._frame)

        self._initialize_upper_part()
        self._initialize_puzzle_list()
        self._initialize_footer()

        self._puzzle_query_frame.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=constants.EW
        )

    def _initialize_footer(self):

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
            command=lambda: PuzzleCreationWindow(self._root, self._add_puzzle)
        )

        add_button.grid(row=3, column=0, columnspan=2)
        cancel_button.grid(row=4, column=0)
        save_button.grid(row=4, column=1)

    def _add_puzzle(self, puzzle):
        self._management_service

    def _initialize_puzzle_list(self):
        if self._puzzle_query_view:
            self._puzzle_query_view.destroy()

        self._puzzle_query_view = PuzzleQueryList(self._puzzle_query_frame, 2)

        self._puzzle_query_view.pack()


    def _initialize_upper_part(self):

        quiz_name_label = ttk.Label(
            master=self._frame,
            text="Visailun nimi:",
            font="Helvetica 10 bold"
        )

        quiz_name_entry = ttk.Entry(master=self._frame)

        quiz_name_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.E)
        quiz_name_entry.grid(row=0, column=1, padx=5, pady=5, sticky=constants.EW)


    def _handle_save_and_return(self):
        # Saving the new quiz to database
        self._puzzle_query_view.pack()
        #self._handle_opening_view()


class PuzzleQueryList:
    """Arvoitusten listaamisesta vastaava näkymä."""
     
    def __init__(self, root, query_count):
        """Luokan konstruktori. Luo uuden arvoituksia listaavan näkymän.

        Args:
            root: TKinter-elementti, joka sisältää ohjelman ikkunan.
            query_count: Alustettavien visailupohjien lukumäärä.
        """

        self._root = root
        self._query_count = query_count
        self._frame = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X, padx=20, pady=20)
    
    def destroy(self):
        """Sulkee näkymän."""
        self._frame.destroy()
    
    def _initialize_puzzle_query(self, order_no):
        puzzle_info_frame = Frame(
            master=self._frame,
            highlightbackground="grey",
            highlightthickness=2)
        
        puzzle_label = ttk.Label(
            master=puzzle_info_frame, 
            text=f"Arvoitus {order_no}",
            font="Helvetica 10 bold"
        )

        name_label = ttk.Label(
            master=puzzle_info_frame, 
            text="Kappaleen nimi: "
        )

        words_label = ttk.Label(
            master=puzzle_info_frame,
            text="Piilotettavat sanat: "
        )

        name_entry = ttk.Entry(master=puzzle_info_frame)
        
        puzzle_label.grid(row=0, column=0, padx=10, pady=10, sticky=constants.EW)
        name_label.grid(row=1, column=0, padx=10, pady=10, sticky=constants.EW)
        name_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky=constants.EW)
        words_label.grid(row=2, column=0, padx=10, pady=0, sticky=constants.EW)

        self._init_puzzle_word_entries(puzzle_info_frame, 5)

        puzzle_info_frame.grid_columnconfigure(0, weight=1)
        puzzle_info_frame.pack(fill=constants.X)
    
    def _init_puzzle_word_entries(self, frame, count):
        for i in range(count):
            entry = ttk.Entry(master=frame, width=10)
            label = ttk.Label(master=frame, text=f"sana{i+1}", font="Helvetica 8 italic")
            
            entry.grid(row=2, column=i+1, padx=10, pady=0)
            label.grid(row=3, column=i+1, padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for i in range(self._query_count):
            self._initialize_puzzle_query(i+1)



class PuzzleCreationWindow:

    def __init__(self, root, handle_add_puzzle):
        self._handle_add_puzzle = handle_add_puzzle
        self._window = Toplevel(root)
        self._window.grab_set()
        self._window.title("Lisää uusi arvoitus")
        self._frame = ttk.Frame(master=self._window)

        self._initialize()

    def _initialize(self):
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
        
        name_label.grid(
            row=0, 
            column=0, 
            columnspan=3, 
            padx=5, 
            pady=(10,0), 
            sticky=constants.W
        )

        name_entry.grid(
            row=1, 
            column=0, 
            columnspan=5, 
            padx=5, 
            pady=5, 
            sticky=constants.EW
        )

        words_label.grid(
            row=2, 
            column=0, 
            columnspan=3, 
            padx=5, 
            pady=(10,5), 
            sticky=constants.W
        )
        
        input_frame.grid(row=0, column=0, columnspan=2)
    
    def _handle_save_changes(self):
        input = self._get_inserted_text()
        error_message = self._handle_add_puzzle(input)
        if error_message:
            print(error_message)

    def _get_inserted_text(self):
        input = []
        input_frame = self._frame.winfo_children()[0]
        info_frame_widgets = input_frame.winfo_children()
        for widget in info_frame_widgets:
            if widget.winfo_class() == "TEntry":
                input.append(widget.get())
        return input
    
    def _init_puzzle_word_entries(self, frame, count):
        for i in range(count):
            entry = ttk.Entry(master=frame, width=10)
            label = ttk.Label(master=frame, text=f"sana{i+1}", font="Helvetica 8 italic")
            
            entry.grid(row=3, column=i, padx=5, pady=0)
            label.grid(row=4, column=i, padx=5, pady=5)
