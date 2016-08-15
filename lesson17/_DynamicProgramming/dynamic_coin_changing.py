"""
Created by JeongMinCha on 2016. 8. 16.
"""
from sys import maxint


def dynamic_coin_changing(C, k):
    """
    17.1: The dynamic algorithm for finding change.
    :param C: list of denominations
    :param k: money for change
    :return: minimum number of coins
    """
    n = len (C)
    dp = [[0] * (k+1) for i in xrange(n+1)]
    dp[0] = [0] + [maxint] * k

    for i in xrange(1, n+1):
        for j in xrange(C[i-1]):
            dp[i][j] = dp[i-1][j]
        for j in xrange(C[i-1], k+1):
            dp[i][j] = min(dp[i][j - C[i-1]] + 1, dp[i-1][j])

    return dp[n]
