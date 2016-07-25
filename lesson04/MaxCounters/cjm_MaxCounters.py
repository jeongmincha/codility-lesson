"""
Created by JeongMinCha on 2016. 7. 26.
"""
def solution(N, A):
    counter = [0] * N

    for e in A:
        if 1 <= e <= N:
            counter[e-1] += 1
        elif e == N+1:
            mx = max(counter)
            counter = [mx] * N

    return counter