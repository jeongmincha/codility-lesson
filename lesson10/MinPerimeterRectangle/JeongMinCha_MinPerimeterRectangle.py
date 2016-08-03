"""
Created by JeongMinCha on 2016. 8. 3.
"""
import math

def solution(N):
    min_perimeter = 1000000000L
    root_N = int(math.sqrt(N))
    for width in range(1, root_N + 1):
        if N % width == 0:
            height = N / width;
            perimeter = (width + height) * 2;
            if min_perimeter > perimeter:
                min_perimeter = perimeter
    return min_perimeter