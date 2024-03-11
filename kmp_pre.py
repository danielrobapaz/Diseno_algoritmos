def lps(s: str) -> str:
    A = [0 for i in range(len(s))]
 
    j = 0
    i = 1
 
    while i < len(s):
        if s[i] == s[j]:
            A[i] = j+1
            j += 1  
            i += 1  
 
        else:  
            if j == 0:  
                i += 1  
 
            else:  
                j = A[j-1]
 
    return s[:A[-1]]