"""
Created by JeongMinCha on 2016. 8. 3.
"""
def solution(N):
    factors = primes(N)
    # key = factor, value = number of the factor
    fact_map = {}

    for factor in factors:
        if fact_map.has_key(factor):
            fact_map[factor] += 1
        else:
            fact_map[factor] = 1

    # Multipliy all of (number of factors + 1)
    num_factors = 1
    for factor in fact_map.keys():
        num_factors *= (fact_map[factor] + 1)

    return num_factors

# Prime Factorization
# e.g. 24 => [2,2,2,3]
def primes(N):
    factors = []
    d = 2
    while d*d <= N:
        while N % d == 0:
            factors.append(d)
            N //= d
        d += 1
    if N > 1:
        factors.append(N)
    return factors