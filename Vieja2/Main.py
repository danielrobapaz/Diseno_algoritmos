from State import State

FIRST_PLAYER = '-'
SECOND_PLAYER = '|'

def primero(s: State, 
            n: int,
            alfa: int,
            beta: int) -> int:
    if n == 0 or not s.has_succesors():
        return -s.eval()

    mejor = float('-inf')
    for _s in s.get_succesors(FIRST_PLAYER):
        mejor = max(mejor, segundo(_s, n-1, alfa, beta))
        alfa = max(alfa, mejor)
        if beta <= alfa:
            break
    return mejor

def segundo(s: State,
            n: int,
            alfa: int,
            beta: int) -> int:
    if n == 0 or not s.has_succesors():
        return s.eval()
    
    mejor = float('inf')
    for _s in s.get_succesors(SECOND_PLAYER):
        mejor = min(mejor, primero(_s, n-1, alfa, beta))
        beta = min(beta, mejor)
        if beta <= alfa:
            break

    return mejor

def main() -> None:
    s = State()
    alfa = float('-inf')
    beta = float('inf')
    n = 100
    print(primero(s, n, alfa, beta))

if __name__ == '__main__':
    main()