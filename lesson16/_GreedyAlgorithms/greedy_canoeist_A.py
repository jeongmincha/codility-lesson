"""
Created by JeongMinCha on 2016. 8. 15.
"""
from collections import deque


def greedyCanoeistA(W, k):
    """
    16.2: Canoeist in O(n) solution.
    :param W: list of weights of canoeists
    :param k: displacement(the maximum load)
    :return: the minimum number of double canoes
    """
    N = len(W)
    heavist = W[-1]  # The heaviest fatso
    skinny = deque()
    fatso = deque()

    for i in xrange(N-1):
        if heavist + W[i] <= k:
            skinny.append(W[i])
        else:
            fatso.append(W[i])
    fatso.append(heavist)

    canoes = 0
    while skinny or fatso:
        if len(skinny) > 0:
            skinny.pop()
        fatso.pop()
        canoes += 1
        if not fatso and skinny:
            fatso.append(skinny.pop())
        while len(fatso) > 1 and fatso[-1] + fatso[0] <= k:
            skinny.append(fatso.popleft())

    return canoes