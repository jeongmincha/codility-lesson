"""
Created by JeongMinCha on 2016. 7. 30.
"""
def solution(A):
    max_so_far = max_ending_here = A[0]

    for idx in range(1, len(A)):
        max_ending_here = max(A[idx], max_ending_here + A[idx])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far