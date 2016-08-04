"""
Created by JeongMinCha on 2016. 8. 4.
"""
def solution(A, B):
    pairs = 0
    for idx in range(len(A)):
        factorA = set(prime_factorization(A[idx]))
        factorB = set(prime_factorization(B[idx]))
        if factorA.issubset(factorB) and factorA.issuperset(factorB):
            pairs +=1
    return pairs

def prime_factorization(N):
    factors = []
    p = 2
    while p * p <= N:
        while N % p == 0:
            factors.append(p)
            N //= p
        p += 1
    if N > 1:
        factors.append(N)
    return factors