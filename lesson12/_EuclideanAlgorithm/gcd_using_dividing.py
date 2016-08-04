def gcd(a, b):
    """
    Greatest common divisor by dividing.
    :param a: An integer to get GCD
    :param b: Another integer to get GCD
    :return: GCD of the input numbers
    """
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)