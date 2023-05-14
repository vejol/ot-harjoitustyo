from ui.game_view import GameView
from ui.opening_view import OpeningView
from ui.edit_view import EditView
from repositories.quiz_repository import QuizRepository
from services.edit_service import EditService
from services.game_service import GameService
from services.management_service import ManagementService
from entities.quiz import Quiz

class UI:
    """Luokka, joka vastaa sovelluksen käyttöliittymästä ja hallitsee eri näkymiä."""
    
    def __init__(self, root):
        """Luokan konstruktori, joka luo uuden käyttöliittymästä vastaavan luokan.

        Args:
            root: TKinter-elementti, joka sisältää ohjelman ikkunan.
        """

        self._root = root
        self._current_view = None

    def start(self):
        """Luo käyttöliittymän aloitusnäkymän."""
        self._show_opening_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _show_create_quiz_view(self, quiz=Quiz("", [])):
        self._hide_current_view()

        self._current_view = EditView(
            self._root,
            self._show_opening_view,
            EditService(quiz, QuizRepository())
        )

        self._current_view.pack()
        self._root.geometry("")

    def _show_game_view(self, quiz):
        self._hide_current_view()


        self._current_view = GameView(
            self._root,
            self._show_opening_view,
            GameService(quiz)
        )
        
        self._current_view.pack()

    def _show_opening_view(self):
        self._hide_current_view()

        self._current_view = OpeningView(
            self._root,
            self._show_game_view,
            self._show_create_quiz_view,
            ManagementService(QuizRepository())
        )

        self._current_view.pack()
