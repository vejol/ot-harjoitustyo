class Puzzle:
    """Luokka, joka kuvaa yksittäistä arvoitusta.
    
    Attributes:
        name: Arvoituksen nimi merkkijonona.
        words: Arvoituksessa piilossa olevat sanat listana.
        order_no: Kokonaisluku, joka kuvaa arvoituksen järjestysnumeroa.
                  Arvoitukset on aina liitetty johonkin visailuun, ja
                  yhdessä visailussa voi olla useampia arvoituksia.
    """

    def __init__(self, name, words, order_no=1):
        """Luokan konstruktori. Luo uuden arvoitusta kuvaavan olion.

        Args:
            name: Arvoituksen nimi merkkijonona.
            words: Arvoitukseen piilotettavat sanat listana.
            order_no: Kokonaisluku, joka kuvaa arvoituksen järjestysnumeroa.
                      Arvoitukset on aina liitetty johonkin visailuun, ja
                      yhdessä visailussa voi olla useampia arvoituksia.
        """

        self.name = name
        self.words = [w.strip().upper() for w in words]
        self.order_no = order_no
