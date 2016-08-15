"""
Created by JeongMinCha on 2016. 8. 15.
"""


def greedyCoinChanging(M, k):
    """
    16.1: The greedy algorithm for finding change.
    :param M: list of denominations
    :param k: money for change
    :return: return list of dict
        (key = denomoniation, value = number of coins)
    """
    n = len(M)
    result = []

    for i in xrange(n-1, -1, -1):
        result += [(M[i], k // M[i])]
        k %= M[i]
    return result
