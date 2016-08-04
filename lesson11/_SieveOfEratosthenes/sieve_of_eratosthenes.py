def sieve(n):
    """
    :param n: An integer representing the upper limit N
    :return: list of primes under given N
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while i*i <= n:
        if sieve[i] is True:
            k = i*i
            while k <= n:
                sieve[k] = False
                k += i
        i += 1
    return sieve