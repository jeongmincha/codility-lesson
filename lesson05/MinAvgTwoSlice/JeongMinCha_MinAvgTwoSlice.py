"""
Created by JeongMinCha on 2016. 7. 26.
"""
def solution(A):
    min_avg = (A[0] + A[1]) / 2.0
    start_pos = 0

    for idx in range(0, len(A)-1):
        avg2slice = (A[idx] + A[idx+1]) / 2.0
        if min_avg > avg2slice:
            min_avg = avg2slice
            start_pos = idx

    for idx in range(0, len(A)-2):
        avg3slice = (A[idx] + A[idx + 1] + A[idx + 2]) / 3.0
        if min_avg > avg3slice:
            min_avg = avg3slice
            start_pos = idx

    return start_pos