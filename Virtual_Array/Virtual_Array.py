import numpy as np
class Virtual_Array:
    def __init__(self, n: int) -> None:
        self.n = n
        self.T = np.empty(shape=(n), dtype='int')
        self.ctr = -1
        self.a = np.empty(shape=(n), dtype='int')
        self.b = np.empty(shape=(n), dtype='int')


    def asignar(self, pos: int, val: int) -> None:
        if pos < 0 or pos >= self.n:
            return False
        
        _, curr_val = self.consultar(pos)

        self.T[pos] = val
        if curr_val is None:
            self.ctr += 1
            self.a[self.ctr] = pos
            self.b[pos] = self.ctr     

        return True  
    
    
    def consultar(self, pos: int):
        if pos < 0 or pos >= self.n:
            return [False, None]

        if not 0 <= self.b[pos] <= self.ctr: 
            return [True, None]
        
        if self.a[self.b[pos]] == pos:
            return [True, self.T[pos]]
        
        return [True, None]

    def limpiar(self) -> None:
        self.ctr = -1
    