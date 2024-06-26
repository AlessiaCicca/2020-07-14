import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        grafo = self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        for nodo in grafo.nodes:
            self._view.dd_squadra.options.append(ft.dropdown.Option(
                               text=nodo))
        self._view.update_page()
    def handle_classifica(self, e):
        squadra= self._view.dd_squadra.value
        if squadra is None:
            self._view.create_alert("Selezionare una squadra")
            return
        vincitrici, perdenti=self._model.classifica(squadra)
        self._view.txt_result.controls.append(ft.Text(f"Le squadre battute da {squadra} con tot: {self._model._idMap[squadra].tot}"))
        for (nodo,diff) in perdenti:
         self._view.txt_result.controls.append(ft.Text(f"{nodo} ({diff})"))
        self._view.txt_result.controls.append(ft.Text(f"Le squadre che hanno battuto {squadra}."))
        for (nodo,diff) in vincitrici:
            self._view.txt_result.controls.append(ft.Text(f"{nodo} ({diff})"))
        self._view.update_page()


