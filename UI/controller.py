import time
from model.model import Model

class Controller:
    def __init__(self, view, model: Model):
        self._view = view
        self._model = model

    def handle_statistiche(self, e):
        serate = 0
        try:
            serate = int(self._view.dd_serate.value)
        except TypeError:
            self._view.avviso(f"Seleziona il numero di serate")
            return
        risultato = self._model.get_statistiche(serate)
        self._view.mostra(risultato)

    def handle_programma(self, e):
        if self._view.dd_serate.value not in ("6", "9", "12"):
            self._view.avviso(f"Seleziona il numero di serate")
            return

        time_start = time.time()
        programma, totale = self._model.get_programma_ottimo(int(self._view.dd_serate.value))

        if not programma:
            self._view.mostra(f"Nessun programma soddisfa i vincoli")
        else:
            self._view.mostra([f"Somma dei voti medi: {totale: .2f}"] + programma)

        time_end = time.time()
        print(f"Time: {time_end - time_start}")