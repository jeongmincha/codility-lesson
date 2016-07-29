"""
Created by JeongMinCha on 2016. 7. 30.
"""
def solution(A):
    max_so_far = A[-1]
    max_profit = 0

    for idx in range(len(A)-1, 0, -1):
        max_profit = max(max_profit, max_so_far-A[idx])
        max_so_far = max(A[idx], max_so_far)

    return max_profit