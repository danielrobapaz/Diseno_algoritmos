class Nodo_segmento:
    def __init__(self, s: str) -> None:
        self.hijo_izquierdo = None
        self.hijo_derecho = None
        self.cadena = s
        self.longitud_maxima_subcadena = 0

    def calcular_maxima_sub_cadena(self):
        pila = [-1]

        longitud_maxima_subcadena = 0

        for i in range(len(self.cadena)):
            if self.cadena[i] == "(":
                pila.append(i)

            else:
                if not pila == []:
                    pila.pop()

                if not pila == []:
                    longitud_maxima_subcadena = max(longitud_maxima_subcadena,
                                                    i - pila[-1])
                    
                else:
                    pila.append(i)

        self.longitud_maxima_subcadena = longitud_maxima_subcadena


def construir_arbol_segmento(S: str) -> Nodo_segmento:
    if len(S) == 0:
        return None
    
    if len(S) == 1:
        return Nodo_segmento(S)
    
    S_prima = construir_arbol_segmento(S[0:len(S)//2])
    S_prima_prima = construir_arbol_segmento(S[len(S)//2:len(S)])

    A = Nodo_segmento(S)
    A.hijo_izquierdo = S_prima
    A.hijo_derecho = S_prima_prima

    A.calcular_maxima_sub_cadena()

    return A