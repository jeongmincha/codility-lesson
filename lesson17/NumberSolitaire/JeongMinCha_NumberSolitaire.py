"""
Created by JeongMinCha on 2016. 8. 16.
"""


def solution(A):
    N = len(A)
    dp = [A[0]] * (N+6)

    for idx in xrange(1, N):
        dp[idx+6] = max(dp[idx:idx+6]) + A[idx]

    return dp[-1]