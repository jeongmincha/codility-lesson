"""
Created by JeongMinCha on 2016. 8. 12.
"""


def solution(A):
    """
    AbsDistinct solution by JeongMinCha
    This method uses the caterpillar method
    :param A: input array
    :return: how many distinct absolute values exist
    """
    beg = 0
    end = len(A) - 1
    abs_distinct = 1
    current = max(abs(A[0]), abs(A[-1]))

    while beg <= end:
        former = abs(A[beg])
        if former == current:
            beg += 1
            continue

        latter = abs(A[end])
        if latter == current:
            end -= 1
            continue

        if former >= latter:
            current = former
            beg += 1
        else:
            current = latter
            end -= 1

        abs_distinct += 1

    return abs_distinct
