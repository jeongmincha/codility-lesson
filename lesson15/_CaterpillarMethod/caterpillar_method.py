"""
Created by JeongMinCha on 2016. 8. 12.
"""


def caterpillarMethod(A, s):
    """
    15.1: Caterpillar in O(n) time complexity.
    :param A: the sequence to find total 's'
    :param s: total value we would like to find
    :return: True if the total which equals to 's' can be found
    """
    n = len(A)
    front, total = 0, 0
    for back in xrange(n):
        while front < n and total + A[front] <= s:
            total += A[front]
            front += 1
        if total == s:
            return True
        total -= A[back]
    return False