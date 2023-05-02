from tkinter import ttk, constants, Frame

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
        query_frame = Frame(
            master=self._frame,
            highlightbackground="grey",
            highlightthickness=2)
        
        puzzle_label = ttk.Label(
            master=query_frame, 
            text=f"Arvoitus {order_no}",
            font="Helvetica 10 bold"
        )

        puzzle_name_label = ttk.Label(
            master=query_frame, 
            text="Kappaleen nimi: "
        )

        puzzle_words_label = ttk.Label(
            master=query_frame,
            text="Piilotettavat sanat: "
        )

        puzzle_name_entry = ttk.Entry(master=query_frame)
        
        puzzle_label.grid(row=0, column=0, padx=10, pady=10, sticky=constants.EW)
        puzzle_name_label.grid(row=1, column=0, padx=10, pady=10, sticky=constants.EW)
        puzzle_name_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky=constants.EW)
        puzzle_words_label.grid(row=2, column=0, padx=10, pady=0, sticky=constants.EW)

        self._init_puzzle_word_entries(query_frame, 5)

        query_frame.grid_columnconfigure(0, weight=1)
        query_frame.pack(fill=constants.X)
    
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


class CreateQuizView:
    """Luokka, joka vastaa visailujen luomiseen tarkoitetusta näkymästä."""

    def __init__(self, root, handle_opening_view):
        """Luokan konstruktori. Luo uuden visailujenluomisnäkymän.

        Args:
            root: TKinter-elementti, joka sisältää ohjelman ikkunan.
            handle_opening_view: Arvo, jota kutsumalla pääsee takaisin aloitusnäkymään.
        """

        self._root = root
        self._handle_opening_view = handle_opening_view
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
        self._initialize_puzzle_query_list()
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

        cancel_button.grid(row=3, column=0)
        save_button.grid(row=3, column=1)

    def _initialize_puzzle_query_list(self):
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