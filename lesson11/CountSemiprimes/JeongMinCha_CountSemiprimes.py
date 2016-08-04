"""
Created by JeongMinCha on 2016. 8. 4.
"""
def solution(N, P, Q):
    num_semiprimes = []

    semi_primes = semi_sieve(N)
    # prefix sum for prime number at the point of the index.
    prefix_sum = []

    # Make prefix sum
    cur_prefix_sum = 0
    for idx in range(0, N+1):
        if idx in semi_primes:
            cur_prefix_sum += 1
        prefix_sum.append(cur_prefix_sum)

    # Using prefix sum, find number of semi primes in given ranges
    for idx in range(0, len(P)):
        start = prefix_sum[P[idx] - 1]
        end = prefix_sum[Q[idx]]
        num_semiprimes.append(end-start)

    return num_semiprimes

# Returns list of semi primes which can be found under given N
def semi_sieve(N):
    semi = set()
    sieve = [True] * (N+1)
    sieve[0] = sieve[1] = False

    # Sieve of Eratosthenes to find primes under given N
    i = 2
    while i*i <= N:
        if sieve[i] is True:
            for j in range(i*i, N+1, i):
                sieve[j] = False
        i+=1
    # Sieve to find semi-primes under given N
    i = 2
    while i*i <= N:
        if sieve[i] is True:
            for j in range(i*i, N+1, i):
                # If i is prime and j/i is also prime, j is semi-prime.
                if j % i == 0 and sieve[j/i] == True:
                    semi.add(j)
        i += 1
    return semi
