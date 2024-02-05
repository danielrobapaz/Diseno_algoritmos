import numpy as np

M = np.array([[0, 1, 0], 
              [0, 0, 1],
              [1, 1, 0]])

def potencia_divide_and_conquer(matrix: np.ndarray,
                                n: int) -> np.ndarray:
    if n == 0:
        return np.identity(3)
    
    p = potencia_divide_and_conquer(matrix, n//2)

    if n % 2 == 0:
        return np.matmul(p, p)
    
    else:
        return np.matmul(matrix, np.matmul(p, p)) 
    
def perrin(n: int) -> int:    
    if n < 0:
        return None
    
    base_cases = np.array([3, 0, 2])

    return int(np.matmul(potencia_divide_and_conquer(M, n), base_cases)[0])