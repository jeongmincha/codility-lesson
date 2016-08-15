"""
Created by JeongMinCha on 2016. 8. 16.
"""

def frog(S, k, q):
    """
    17.3: Solution in time complexity O(nk) and space complexity O(k)
    :param S: fixed distanes
    :param k: position to jump
    :param q: modulo q for avoiding overflow
    :return: number of different ways the frong can jump to k
    """
    n = len(S)
    dp = [1] + [0] * k

    for j in xrange(1, k+1):
        for i in xrange(n):
            if S[i] <= j:
                dp[j] = (dp[j] + dp[j - S[i]]) % q

    return dp[k]
