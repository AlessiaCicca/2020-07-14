import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()


    def creaGrafo(self):
        self._idMap = {}
        self.nodi = DAO.getNodi()
        self.grafo.add_nodes_from(self.nodi)
        for v in self.nodi:
            self._idMap[v.Name] = v
        self.addEdges()
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self):
        self.grafo.clear_edges()
        for nodo1 in self.grafo:
            for nodo2 in self.grafo:
                if nodo1 != nodo2 and self.grafo.has_edge(nodo1, nodo2) == False:
                    delta=nodo1.tot-nodo2.tot
                    if delta>0:
                        self.grafo.add_edge(nodo1, nodo2, weight=abs(delta))
                    if delta<0:
                        self.grafo.add_edge(nodo2, nodo1, weight=abs(delta))
    def classifica(self, squadraNome):
        squadra=self._idMap[squadraNome]
        vin=[]
        per=[]
        for nodo in self.grafo.nodes:
            if nodo.tot>squadra.tot:
                vin.append((nodo, nodo.tot-squadra.tot))
            if nodo.tot<squadra.tot:
                per.append((nodo, -nodo.tot+squadra.tot))
        return sorted(vin,key=lambda x:x[1]),  sorted(per,key=lambda x:x[1])


