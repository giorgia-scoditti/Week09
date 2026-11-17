from database.dao import Dao

class Model:

    def __init__(self):
        pass

    def get_staistiche(self, serate):
        return Dao.read_statistiche(serate)

    def get_programma_ottimo(self, serate):
        lista_film = Dao.read_statistiche(serate)
        # Qui dovrei determinare il programma ottimo usando serate e lista_film.
        # Uso una strategia ricorsiva.
        if True:
            pass
        else:
            pass
        # Restituisco il programma ottimo.