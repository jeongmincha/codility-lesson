"""
Created by JeongMinCha on 2016. 7. 30.
"""
def solution(A):
    max_ending_here = [0] * len(A)
    max_starting_here = [0] * len(A)

    max_so_far1 = 0
    for idx in range(1, len(A)-1):
        max_so_far1 = max(0, A[idx] + max_so_far1)
        max_ending_here[idx] = max_so_far1

    max_so_far2 = 0
    for idx in range(len(A)-2, 0, -1):
        max_so_far2 = max(0, A[idx] + max_so_far2)
        max_starting_here[idx] = max_so_far2

    max_double_slice = 0
    for idx in range(0, len(A)-2):
        max_double_slice = max(max_double_slice, max_ending_here[idx] + max_starting_here[idx+2])

    return max_double_slice