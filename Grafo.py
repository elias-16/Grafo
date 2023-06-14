from collections import deque

class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []

    def adicionar_aresta(self, vertice_origem, vertice_destino):
        if vertice_origem in self.grafo:
            self.grafo[vertice_origem].append(vertice_destino)
        else:
            self.grafo[vertice_origem] = [vertice_destino]

    def dfs(self, vertice_inicial):
        visitados = set()

        def dfs_recursiva(vertice):
            visitados.add(vertice)
            print(vertice, end=' ')

            for vizinho in self.grafo[vertice]:
                if vizinho not in visitados:
                    dfs_recursiva(vizinho)

        dfs_recursiva(vertice_inicial)
        print()

    def bfs(self, vertice_inicial):
        visitados = set()
        fila = deque([vertice_inicial])

        while fila:
            vertice = fila.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                print(vertice, end=' ')

                for vizinho in self.grafo[vertice]:
                    if vizinho not in visitados:
                        fila.append(vizinho)

        print()


# Testando...
grafo = Grafo()
grafo.adicionar_vertice('A')
grafo.adicionar_vertice('B')
grafo.adicionar_vertice('C')
grafo.adicionar_vertice('D')
grafo.adicionar_vertice('E')
grafo.adicionar_aresta('A', 'B')
grafo.adicionar_aresta('A', 'C')
grafo.adicionar_aresta('B', 'D')
grafo.adicionar_aresta('B', 'E')

print("Busca em Profundidade (DFS):")
grafo.dfs('A')

print("Busca em Largura (BFS):")
grafo.bfs('A')