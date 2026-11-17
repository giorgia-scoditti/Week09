from model.model import Model

class Controller:
    def __init__(self, view, model: Model):
        self._view = view
        self._model = model

    def handle_statistiche(self, e):
        serate = int(self._view.dd_serate.value)
        risultato = self._model.get_staistiche(serate)
        self._view.mostra(risultato)

    def handle_programma(self, e):
        serate =  int(self._view.dd_serate.value)
        risultato = self._model.get_programma_ottimo(serate)