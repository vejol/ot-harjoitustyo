from tkinter import ttk, constants, Listbox, messagebox
from services.management_service import management_service

class OpeningView:

    def __init__(self, root, hande_game_view, handle_new_quiz_view):
        self._root = root
        self._handle_game_view = hande_game_view
        self._handle_new_quiz_view = handle_new_quiz_view
        self._frame = None

        self._initialize()
    
    def destroy(self):
        self._frame.destroy()

    def __selected_quiz(self):
        value = self.__quiz_list.curselection()

        if not value:
            return None
        
        return self.__quiz_list.get(value)


    def pack(self):
        self._frame.pack(fill=constants.X)
            
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        start_game_button = ttk.Button(
            master=self._frame,
            text="Aloita peli",
            command=self.__start_game_action
        )

        create_quiz_button = ttk.Button(
            master=self._frame,
            text="Luo uusi peli",
            command=self._handle_new_quiz_view
        )

        welcome_label = ttk.Label(
            master=self._frame, 
            text="Tervetuloa pelaamaan Musiikkivisaa!",
            font=("Helvetica", 25)
        )
        
        self.__quiz_list = Listbox(
            master=self._frame
        )

        quiz_names = management_service.find_quiz_names()

        for counter, quiz_name in enumerate(quiz_names):
            self.__quiz_list.insert(counter, quiz_name)

        welcome_label.grid(row=0, column=0, columnspan=2)
        self.__quiz_list.grid(row=1, column=0, columnspan=2)
        start_game_button.grid(row=2, column=0)
        create_quiz_button.grid(row=2, column=1)
    
    def _show_quiz_messagebox(self):
        messagebox.showinfo(title="Valitse visailu", message="Valitse ensin haluamasi visailu listalta!")

    def __start_game_action(self):
        selection = self.__selected_quiz()

        if not selection:
            self._show_quiz_messagebox()
            return
    
        self._handle_game_view(management_service.find_quiz(selection))
