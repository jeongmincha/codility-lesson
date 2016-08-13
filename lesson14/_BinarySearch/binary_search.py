"""
Created by JeongMinCha on 2016. 8. 10.
"""
def binarySearch(A, x):
    """
    14.1: Binary Search in O(log n)
    :param A: list of sorted numbers
    :param x: the number to search
    :return: the index of the found number
    """
    n = len(A)
    beg = 0
    end = n - 1
    result = -1

    while beg <= end:
        mid = (beg + end) / 2
        if A[mid] <= x:
            beg = mid + 1
            result = mid
        else:
            end = mid - 1

    return result