"""
Created by JeongMinCha on 2016. 8. 3.
"""
import math, sys

def solution(N):
    min_perimeter = sys.maxint

    root_N = int(math.sqrt(N))
    for width in range(1, root_N + 1):
        if N % width == 0:
            height = N / width;
            perimeter = (width + height) * 2;
            if min_perimeter > perimeter:
                min_perimeter = perimeter
    return min_perimeter