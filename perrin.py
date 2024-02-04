import numpy as np

M = np.array([[0, 1, 0], 
              [0, 0, 1],
              [1, 1, 0]])

def potencia_divide_and_conquer(matrix: np.ndarray,
                                n: int) -> np.ndarray:
    print(n)
    
    if n == 0:
        return np.identity(3)
    
    if n == 1:
        return matrix
    
    p = potencia_divide_and_conquer(matrix, n//2)

    if n % 2 == 0:
        return np.matmul(p, p)
    
    else:
        return np.matmul(p, np.matmul(p, p)) 
    
def perrin(n: int) -> int:    
    if n < 0:
        return None
    
    elif n == 0:
        return 3
    
    elif n == 1:
        return 0
    
    elif n == 2:
        return 2
    
    base_cases = np.array([3, 0, 2])

    return np.matmul(potencia_divide_and_conquer(M, n), base_cases)

print(potencia_divide_and_conquer(M, 5))


res = np.identity(3)

for i in range(5):
    res = np.matmul(res, M)

print(res)