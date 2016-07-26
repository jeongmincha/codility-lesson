"""
Created by JeongMinCha on 2016. 7. 27.
"""
def solution(A):
    A.sort()
    return max(A[0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])
