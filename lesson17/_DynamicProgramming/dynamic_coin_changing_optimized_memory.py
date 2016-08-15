"""
Created by JeongMinCha on 2016. 8. 16.
"""
from sys import maxint


def dynamic_coin_changing(C, k):
    """
    17.2: The dynamic algorithm for finding change with optimized memory
    :param C: list of denominations
    :param k: money for change
    :return: minimum number of coins
    """
    n = len (C)
    dp = [0] + [maxint] * k

    for i in xrange(1, n+1):
        for j in xrange(C[i-1], k+1):
            dp[j] = min(dp[j - C[i-1]] + 1, dp[j])

    return dp
