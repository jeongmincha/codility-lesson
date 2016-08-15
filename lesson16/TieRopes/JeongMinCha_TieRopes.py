"""
Created by JeongMinCha on 2016. 8. 15.
"""


def solution(K, A):
    ropes = 0
    cur_length = 0
    for idx in xrange(len(A)):
        cur_length += A[idx]
        if cur_length >= K:
            cur_length = 0
            ropes += 1

    return ropes