"""
Created by JeongMinCha on 2016. 8. 12.
"""


def solution(A):
    num_triangle = 0
    N = len(A)
    sA = sorted(A)

    for x in xrange(N):
        z = x + 2
        for y in xrange(x+1, N):
            while z < N and sA[x] + sA[y] > sA[z]:
                z += 1
            num_triangle += z - y - 1

    return num_triangle