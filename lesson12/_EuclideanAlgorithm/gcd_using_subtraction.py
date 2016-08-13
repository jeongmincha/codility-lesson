def gcd(a, b):
    """
    Greatest common divisor by subtraction
    :param a: An integer to get GCD
    :param b: Another integer to get GCD
    :return: GCD of the input numbers
    """
    if a == b:
        return a
    if a > b:
        return gcd (a - b, b)
    else:
        return gcd (a, b - a)