# -*- coding: utf-8 -*-
"""
Created by JeongMinCha on 2016. 8. 10

Problem: You are given n binary values x0, x1, . . . , xn−1,
such that xi ∈ {0, 1}. This array represents holes in a roof
(1 is a hole). You are also given k boards of the same size.
The goal is to choose the optimal (minimal) size of the boards
that allows all the holes to be covered by boards..
"""


def boards(A, k):
    """
    14.2: Binary Search in O(log n)
    :param A: list of binary values (1 = hole, 0 = normal)
    :param k: size of boards
    :return: optimal size of the boards
    """
    n = len(A)
    beg = 1
    end = n
    result = -1

    while beg <= end:
        mid = (beg + end) / 2
        if check(A, mid) <= k:
            end = mid - 1
            result = mid
        else:
            beg = mid + 1
    return result


def check(A, k):
    """
    14.3: Greedily check in O(n)
    :param A: list of binary values (1 = hole, 0 = normal)
    :param k: size of boards
    :return: number of boards
    """
    n = len(A)
    boards = 0
    last = -1

    for i in xrange(n):
        # if this position has a hole and
        # any board doesn't cover the hole
        if A[i] == 1 and last < i:
            boards += 1
            last = i + k - 1
    return boards