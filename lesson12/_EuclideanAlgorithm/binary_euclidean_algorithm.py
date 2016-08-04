def gcd(a, b, res):
    """
    Greatest common divisor using binary Euclidean algorithm.
    :param a: An integer to get GCD
    :param b: Another inger to get GCD
    :param res: to keep result when result gets lower than we thought.
    :return: GCD of a, b
    """
    if a == b:
        return res * a
    elif a % 2 == 0 and b % 2 == 0:
        return gcd(a/2, b/2, 2 * res)
    elif a % 2 == 0:
        return gcd(a/2, b, res)
    elif b % 2 == 0:
        return gcd(a, b/2, res)
    elif a > b:
        return gcd(a - b, b, res)
    else:
        return gcd(a, b - a, res)