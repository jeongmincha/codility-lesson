"""
Created by JeongMinCha on 2016. 7. 27.
"""
def solution(A):
    num_intersect = 0

    upperbound = [0] * len(A)
    lowerbound = [0] * len(A)

    for idx in range(0, len(A)):
        upperbound[idx] = idx + A[idx]
        lowerbound[idx] = idx - A[idx]

    upperbound.sort()
    lowerbound.sort()

    lower_idx = 0
    for upper_idx in range(0,len(upperbound)):
        while lower_idx < len(A) and upperbound[upper_idx] >= lowerbound[lower_idx]:
            lower_idx += 1
        num_intersect += (lower_idx - 1) - upper_idx
        if num_intersect > 10000000:
            return -1

    return num_intersect