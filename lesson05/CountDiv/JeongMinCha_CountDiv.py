"""
Created by JeongMinCha on 2016. 7. 26.
"""
def solution(A, B, K):
    if A%K == 0:
        return (B-A)/K + 1
    else:
        return (B-(A-A%K))/K