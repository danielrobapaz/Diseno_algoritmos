# Implementacion de un algoritmo voraz que resuelve el siguiente problema
# 
# Dadas n peticiones de publcidad, donde la i-esima peticion tiene p_i (el punto de inicio de 
# la valla) y t_i (el tamano de la valla), se debe de escoger un conjunto maximal de peticiones tal que 
# ninguna valla intersecte con otra.
#
# El algoritmo debe usar tiempo O(n log n) y memoria adicional O(n).

def vallas_publicitarias(P: [[int, int]]) -> [[int, int]]:
    P_prima = [[p[0], p[0]+p[1]] for p in P]

    P_prima = sorted(P_prima, key=lambda p: p[1])
    
    R = []

    i = 0

    while (i < len(P_prima)-1):
        R.append(P_prima[i]) # tiene un costo amortizado de O(1)

        # verificar si se intersectan
        if P_prima[i][1] > P_prima[i+1][0]:
            i += 1

        i += 1

    if R[-1][1] <= P_prima[-1][0]:
        R.append(P_prima[-1])
    
    return [[r[0], r[1]-r[0]] for r in R]

print(vallas_publicitarias([[1, 3], [1, 2], [3, 5], [9,1], [11, 1], [10, 2]]))


