"""
Created by JeongMinCha on 2016. 8. 15.
"""


def greedyCanoeistB(W, k):
    """
    16.3: Canoeist in O(n) solution.
    :param W: list of weights of canoeists
    :param k: displacement (the maximum load)
    :return: the minimum number of double canoes
    """
    canoes = 0
    j = 0
    i = len(W) - 1

    while j <= i:
        if W[i] + W[j] <= k:
            j += i
        canoes += 1
        i -= 1

    return canoes