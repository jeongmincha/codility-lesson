"""
Created by JeongMinCha on 2016. 7. 26.
"""
def solution(A, B, K):
    ret = 0
    for elem in range(A, B+1):
        if elem % K == 0:
            ret += 1
    return ret