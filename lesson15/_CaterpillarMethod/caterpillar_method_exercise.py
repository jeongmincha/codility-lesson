"""
Created by JeongMinCha on 2016. 8. 12.
"""

def triangles(A):
    """
    15.2: The number of triangles in O(n^2).
    :param A: n sticks to construct triangles
    :return: the number of triangles that can be constructed
    """
    n = len(A)
    result = 0
    for x in xrange(n):
        z = x + 2
        for y in xrange(x+1, n):
            while z < n and A[x] + A[y] > A[z]:
                z += 1
            result += z - y - 1
    return result