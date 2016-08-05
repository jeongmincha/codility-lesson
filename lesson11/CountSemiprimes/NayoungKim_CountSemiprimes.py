def solution(N, P, Q):
    n = N
    l = Q[0] - P[0]
    F = [0] * (n+1)
    i = 2
    result = [0]*len(P)
    temp = 0
    while i * i <= n:
        if F[i] == 0:
            k = i * i
            while k <= n:
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1
    
    for a in range(0,len(P)):
        for j in range(2,n):
            for k in range(j,n):
                if F[j] == 0 and F[k]==0:
                    temp = j * k
                    if temp >= P[a] and temp <= Q[a]:
                        result[a] += 1
                    
    return result