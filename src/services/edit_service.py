import copy
from entities.puzzle import Puzzle
from entities.quiz import Quiz
from repositories.quiz_repository import QuizRepository
from services.management_service import management_service


class EditService:
    """Luokka, joka vastaa visailujen muokkaamiseen tarvittavasta logiikasta.
        EditService tarjoaa tarvittavat palvelut visailujen luomiseen, muokkaamiseen
        sekä poistamiseen. Lisäksi se pitää kirjaa muokkaamisprosessin sen hetkisestä
        tilasta eli esimerkiksi siitä, mitä arvoituksia kyseiseen visailuun on liitetty.
    """

    def __init__(self, old_quiz: Quiz):
        """Luokan konstruktori. Luo uuden visailujen muokkaamislogiikasta vastaavan palvelun.

        Args:
            old_quiz (Quiz): Quiz-olio, joka kuvaa muokattavaa visailua. Palvelu luo tästä
                                ensin kopion, johon muutokset tehdään siltä varalta, että 
                                käyttäjä haluaakin peruuttaa tehdyt muutokset.
        """
        self._repository = QuizRepository()
        self._old_quiz = old_quiz
        self._quiz = copy.deepcopy(old_quiz)

    def get_name(self):
        """Palauttaa muokattavaksi annetun visailun nimen.

        Returns:
            srt: Merkkijono, joka kuvaa muokattavaksi annetun visailun nimeä. Jos 
                 ollaan luomassa uutta visailua, merkkijono on tyhjä.
        """
        return self._quiz.name

    def set_name(self, name: str):
        """Tarkistaa, onko visailulle annettu nimi kelvollinen ja uniikki. Jos ehdot
            täyttyvät, annettu nimi asetetaan luotavan olion nimeksi.

        Args:
            name (str): Merkkijono, joka kuvaa visailun nimeä.

        Raises:
            NoQuizNameError: Virhe, joka tapahtuu, jos annettu merkkijono on tyhjä.
            QuizExistError: Virhe, joka seuraa, jos tietokannassa on jo saman niminen
                            visailu.
        """
        name = name.strip()

        if name == "":
            raise NoQuizNameError("Quiz name is missing.")

        old_name = self._old_quiz.name
        quiz_names = management_service.get_quiz_names()

        if name in quiz_names and name != old_name:
            raise QuizExistError("A quiz with same name already exists.")

        self._quiz.name = name

    def get_puzzles(self):
        """Palauttaa listan, joka sisältää luotavan visailun arvoitukset.

        Returns:
            list: Lista, joka sisältää luotavan visailun arvoitukset Puzzle-olioina.
        """
        return self._quiz.puzzles

    def add_puzzle(self, user_input):
        """Lisää luotavaan visailuun uuden arvoituksen käyttäjän syötteen perusteella.

        Args:
            user_input (list): Lista, joka sisältää käyttäjän PuzzleCreationWindow-
                               näkymässä antaman syötteen.
        """
        name = user_input.pop(0)
        words = user_input
        puzzle = Puzzle(name, words)

        self._quiz.puzzles.append(puzzle)

    def remove_puzzle(self, index):
        """Poistaa annetun indeksin osoittaman arvoituksen luotavasta visailusta.

        Args:
            index (int): Kokonaisluku, joka osoittaa poistettavan arvoituksen indeksin.
        """
        self._quiz.puzzles.pop(index)

    def save_quiz(self):
        """Tallentaa luotavana olevan visailun tietokantaan."""
        
        if self._old_quiz.name != "":
            self._repository.delete_quiz(self._old_quiz)

        self._repository.save_quiz(self._quiz)


class QuizExistError(Exception):
    pass

class NoQuizNameError(Exception):
    pass
