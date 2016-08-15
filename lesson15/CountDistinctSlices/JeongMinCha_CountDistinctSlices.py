"""
Created by JeongMinCha on 2016. 8. 12.
"""


def solution(M, A):
    distinct_slices = 0
    N = len(A)
    front = back = 0
    seen = [False] * (M+1)

    while front < N and back < N:
        while front < N and seen[A[front]] == False:
            distinct_slices += front - back + 1
            seen[A[front]] = True
            front += 1
        else:
            while front < N and back < N and A[back] != A[front]:
                seen[A[back]] = False
                back += 1
            seen[A[back]] = False
            back += 1

    return min(distinct_slices, 1000000000)