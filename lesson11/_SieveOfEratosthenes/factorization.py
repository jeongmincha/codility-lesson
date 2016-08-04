def factorization(x, F):
    primeFactors = []
    while F[x] > 0:
        primeFactors += [F[x]]
        x /= F[x]
    primeFactors += [x]
    return primeFactors