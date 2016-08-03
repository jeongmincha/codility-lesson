"""
Created by JeongMinCha on 2016. 8. 3.
"""
from math import sqrt

def solution(A):
    num_peaks = 0
    first_peak = -1
    next_peak = [-1] * len(A)

    for idx in range(len(A)-2, 0, -1):
        if A[idx] > max(A[idx+1], A[idx-1]):
            next_peak[idx] = idx
            num_peaks += 1
            first_peak = idx
        else:
            next_peak[idx] = next_peak[idx+1]
    if num_peaks < 2:
        return num_peaks

    max_flags = 1
    max_min_distance = int(sqrt(len(A)))
    for min_distance in range(max_min_distance+1, 1, -1):
        used_flags = 1
        rest_flags = min_distance-1
        pos = first_peak
        while rest_flags > 0:
            if pos + min_distance >= len(A)-1:
                break
            pos = next_peak[pos+min_distance]
            if pos == -1:
                break;
            used_flags += 1
            rest_flags -= 1
        max_flags = max(max_flags, used_flags)

    return max_flags