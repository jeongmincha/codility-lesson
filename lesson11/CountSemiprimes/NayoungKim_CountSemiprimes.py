def sieve(n):
    sieve = [True] * (n + 1)
    semi = set()
    sieve[0] = sieve[1] = False
    i = 2
    while i * i <= n:
        if sieve[i]:
            k = i * i
            while k <= n:
                sieve[k] = False
                k += i
        i += 1
    i = 2
    while i * i <= n:
        if sieve[i] == True:
            for j in xrange(i*i, n+1, i):
                if sieve[j/i]==True:
                    semi.add(j)
        i += 1
            
    return semi

def solution(N, P, Q):
    semi = sieve(N)
    count = []
    count.append(0) # 0
    count.append(0) # 1
    count.append(0) # 2
    count.append(0) # 3
    count.append(1) # 4
    
    for i in xrange(5, max(Q)+1):
        if i in semi:
            count.append(count[-1]+1)
        else:
            count.append(count[-1])
    
    result = []
    for i in xrange(len(Q)):
        result.append(count[Q[i]] - count[P[i]-1])
    return result