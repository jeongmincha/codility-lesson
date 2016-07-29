"""
Created by JeongMinCha on 2016. 7. 30.
"""
def solution(A):
    if len(A) < 2:
        return 0

    max_so_far = A[-1]
    max_profit = 0

    for idx in range(len(A)-2, -1, -1):
        max_profit = max(max_profit, max_so_far-A[idx])
        max_so_far = max(A[idx], max_so_far)

    return max_profit