from database.dao import Dao

class Model:

    def __init__(self):
        self._miglior_programma = []
        self._miglior_punteggio = -1 # Valore di default: mi serve per fare le verifiche.

    def get_statistiche(self, serate):
        return Dao.read_statistiche(serate)

    def get_programma_ottimo(self, serate):
        lista_film_serate = Dao.read_film_serate(serate)
        for f in lista_film_serate:
            print(f)

        # Facendo come di seguito, evito di sovrascrivere i dati.
        self._miglior_programma = []
        self._miglior_punteggio = -1

        # Qui dovrei determinare il programma ottimo usando serate e lista_film_serate.
        # Uso una strategia ricorsiva.
        self._ricorsione([], lista_film_serate, serate)
        if self._miglior_punteggio == -1:
            return [], 0

        # Restituisco il programma ottimo.
        return self._miglior_programma, self._miglior_punteggio

    def _ricorsione(self, parziale, lista_film_serate, serate):
        # 1. Termino la ricorsione.
        if len(parziale) == serate: # Vincolo assoluto.
            punteggio = self._calcola_punteggio(parziale)

            if punteggio > self._miglior_punteggio:
                self._miglior_punteggio = punteggio
                self._miglior_programma = parziale.copy() # ATTENZIONE AL COPY! Senza quello, non mi creo una lista nuova.
            return

        serata = len(parziale) + 1

        # 2. Mi occupo di tutte le varie casistiche.
        for film in lista_film_serate[(serata - 1) * 4 : serata * 4]:
            if self._vincoli_soddisfatti(parziale, film, serate):
                parziale.append(film)
                self._ricorsione(parziale, lista_film_serate, serate)
                parziale.pop()

    def _vincoli_soddisfatti(self, parziale, film, serate):
        # Requisito 1: due film consecutivi non possono avere lo stesso genere.
        if len(parziale) > 0:
            if parziale[-1].genere == film.genere:
                return False

        # Requisito 2: un genere non può comparire più di due volte.
        occorrenze = 0
        for scelto in parziale:
            if scelto.genere == film.genere:
                occorrenze += 1

        if occorrenze >= 2:
            return False

        # Requisiti ulteriori: sono vincoli che si possono fare alla fine di tutto.
        if len(parziale) + 1 == serate:
            num_commedie = 0
            generi_diversi = set()

            for scelto in parziale:
                if scelto.genere == "Comedy":
                    num_commedie += 1
                generi_diversi.add(scelto.genere)

            if film.genere == "Comedy":
                num_commedie += 1
            generi_diversi.add(film.genere)

            if num_commedie < 2 or len(generi_diversi) < 3:
                return False
        return True

    def _calcola_punteggio(self, programma):
        punteggio = 0
        for film in programma:
            punteggio += film.media
        return punteggio