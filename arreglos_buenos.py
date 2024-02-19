def subarreglos_buenos(A: list[int]) -> int:
    _A  = [0] + A
    N = len(A)
    prev = [0] + ([1] * N)
    res = N

    for j in range(2, N+1):
        curr = [0] * (N+1)
        for i in range(j, N+1):
            if _A[i] % j == 0:
                curr[i] = sum(prev[:i])
        prev = curr[:]
        res += sum(curr)

    return res

print(subarreglos_buenos([1,2,1,1,1,6]))
