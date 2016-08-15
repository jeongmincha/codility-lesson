"""
Created by JeongMinCha on 2016. 8. 15.
"""


def solution(A, B):
    N = len(A)
    if N < 2:
        return N

    count = 1
    end = B[0]
    index = 1

    while index < N:
        while index < N and A[index] <= end:
            index += 1

        if index == N:
            break

        count += 1
        end = B[index]

    return count
