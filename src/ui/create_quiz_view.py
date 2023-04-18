from tkinter import ttk, constants


class CreateQuizView:

    def __init__(self, root, handle_opening_view):
        self._root = root
        self._handle_opening_view = handle_opening_view
        self._frame = None

        self._initialize()

    def destroy(self):
        self._frame.destroy()

    def pack(self):
            self._frame.pack(fill=constants.X)
                
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        cancel_button = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=self._handle_opening_view
        )

        save_button = ttk.Button(
            master=self._frame,
            text="Save",
            command=self._save_and_return
        )

        cancel_button.grid(row=0, column=0)
        save_button.grid(row=0, column=1)


    def _save_and_return(self):
         # Saving the new quiz to database
         self._handle_opening_view()