"""
Created by JeongMinCha on 2016. 7. 27.
"""
def solution(A):
    if len(A) < 3:
        return 0
    A.sort()
    if A[-1] < 0:
        return 0

    for idx in range(0, len(A)-2):
        if A[idx] + A[idx+1] > A[idx+2]:
            return 1
    return 0