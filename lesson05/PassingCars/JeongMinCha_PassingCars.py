"""
Created by JeongMinCha on 2016. 7. 21.
"""
def solution(A):
    MAXIMUM = 1000000000
    passing = 0
    east = 0
    for elem in A:
        if elem == 0:
            east += 1
        else:
            passing += east
            if passing > MAXIMUM:
                return -1
    return passing