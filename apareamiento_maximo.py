from queue import Queue

INF = 2147483647
NIL = 0

class Grafo():
    def __init__(self, m, n):
        self.__m = m
        self.__n = n
        
        # representacion usando listas de adyancencias
        self.__adj = [[] for _ in range(m+1)]
 
    def agregar_lado(self, u, v):
        self.__adj[u].append(v)

    def lado(self):
        return self.__adj
    
    def hay_camino_de_aumento(self):
        Q = Queue()
        for u in range(1, self.__m+1):
            if self.__pairU[u] == NIL:
                # u no ha sido apareado
                self.__dist[u] = 0
                Q.put(u)
            
            else:
                self.__dist[u] = INF
        
        self.__dist[NIL] = INF

        # Q contiene los vertices de uno de los conjuntos del grafo
        # sin perdida de generalidad, los el conjuto izquierdo
        while not Q.empty():
            u = Q.get()
            if self.__dist[u] < self.__dist[NIL]:
                for v in self.__adj[u]:

                    if self.__dist[self.__pairV[v]] == INF:
                        self.__dist[self.__pairV[v]] = self.__dist[u] + 1
                        Q.put(self.__pairV[v])
        return self.__dist[NIL] != INF
 
    
    def hay_camino_de_aumento_desde(self, u):
        if u != NIL:
            for v in self.__adj[u]:
                if self.__dist[self.__pairV[v]] == self.__dist[u] + 1:
                    if self.hay_camino_de_aumento_desde(self.__pairV[v]):
                        self.__pairV[v] = u
                        self.__pairU[u] = v
                        return True
            self.__dist[u] = INF
            return False
        return True
 
    def hopcroft_karp(self):
        # implementa el algoritmo de hopcroftKarp
        # y devuelve la cantidad de lados del apareamiento
        # maximo del grafo


        # Inicializamos arreglos
        self.__pairU = [0 for _ in range(self.__m+1)]
        self.__pairV = [0 for _ in range(self.__n+1)]
        self.__dist = [0 for _ in range(self.__m+1)]
        
        result = 0
 
        while self.hay_camino_de_aumento():
            for u in range(1, self.__m+1):
                if self.__pairU[u] == NIL and self.hay_camino_de_aumento_desde(u):
                    result += 1

        return result


def es_primo(n: int):
    if n<=1:
        return False
    
    for _n in range(2, int(n**0.5) + 1):
        if n % _n == 0:
            return False
        
    return True

def construir_grafo(C: list[int]):

    pares = [c for c in C if c%2 == 0]
    impares = [c for c in C if c%2 != 0]

    m = len(pares)
    n = len(impares)

    g = Grafo(m, n)

    for u in range(len(pares)):
        for v in range(len(impares)):
            if es_primo(pares[u]+impares[v]):
                g.agregar_lado(u, v)

    return g

def obtener_cantidad_minima_elementos(C: list[int]) -> int:
    g = construir_grafo(C)

    return g.hopcroft_karp()


print(obtener_cantidad_minima_elementos([1, 2, 3, 4, 5, 11]))