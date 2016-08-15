"""
Created by JeongMinCha on 2016. 8. 15.
"""


def solution(A):
    A.sort()

    if A[0] >= 0:
        return 2 * A[0]
    if A[-1] <= 0:
        return -2 * A[-1]

    front, back = len(A)-1, 0
    minAbs = 2 * A[-1]

    while back <= front:
        cur = abs(A[back] + A[front])
        if minAbs > cur:
            minAbs = cur

        if abs(A[back+1] + A[front]) <= cur:
            back += 1
        elif abs(A[back] + A[front-1]) <= cur:
            front -= 1
        else:
            back += 1; front -= 1

    return minAbs
