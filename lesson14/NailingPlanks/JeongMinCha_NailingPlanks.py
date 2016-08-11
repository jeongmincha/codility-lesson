"""
Created by JeongMinCha on 2016. 8. 10.
"""

def _findFirstNail(plankBegin, plankEnd, nails, preResult):
    # Function: find the nails, that could nail this plank.
    #
    # Input: plankBegin: the begin position of current plank
    #        plankEnd: the end position of current plank
    #        nails: the nails' position and index
    #        preResult: for all of the previous planks, the
    #           first preResult+1 nails in original array
    #           could be sequentially used to nail them.
    #
    # Return: If all these nails are after the preResult's
    #       position, return the first nail's position in
    #       the original nails' array.
    #       Else, return the preResult as the result.

    result = -1     # The index of nail in the original array
    resultPos = -1  # The index of nail in the sorted array

    nailLower = 0
    nailUpper = len(nails) - 1
    nailMid = 0

    # Find the first nail, whose postion >= plankBegin and
    #   position <= plankEnd, with binary search algorithm
    while nailLower <= nailUpper:
        nailMid = (nailLower + nailUpper) / 2
        nailPosMid = nails[nailMid][1]
        if nailPosMid < plankBegin:
            nailLower = nailMid + 1
        elif nailPosMid > plankEnd:
            nailUpper = nailMid - 1
        else:
            nailUpper = nailMid - 1
            result = nails[nailMid][0]
            resultPos = nailMid

    # Cannot find one, which could nail the plank
    if result == -1:                        return -1

    # Linear search all the quanlified nails, and find
    # out the one with the earliest position.
    resultPos += 1
    while resultPos < len(nails):
        # Not quanlified anymore.
        if nails[resultPos][1] > plankEnd:  break
        result = min(result, nails[resultPos][0])
        resultPos += 1
        # If we find a position before the preResult. We could
        # terminate our search and return.
        # With a position before the preResult, the result for
        # this round must <= preResult. And globally, the final
        # result is the maximum of ALL the results in each rounds.
        # So the result of this round actually does not affect
        # the final result.
        if preResult >= result:             return preResult

    return max(result, preResult)

def solution(A, B, C):
    # Sort the nails according to their positions
    nails = sorted(enumerate(C), key = lambda x: x[1])
    result = -1

    for plankIndex in xrange(len(A)):
        # Find a nail for the current plank
        result = _findFirstNail(A[plankIndex], B[plankIndex], nails, result)
        if result == -1:  return -1     # Cannot find such a nail

    return result + 1