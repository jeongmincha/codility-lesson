"""
Created by JeongMinCha on 2016. 8. 3.
"""
def solution(A):
    peak_idxs = peak_idxs_in(A)
    num_peak = len(peak_idxs)

    max_num_groups = 0
    for groups in range(1, num_peak + 2):
        if len(A) % groups == 0:
            size = len(A) / groups
            find = []
            for peak in peak_idxs:
                find.append(peak/size)
            find = set(find)
            if len(find) != groups:
                return max_num_groups
            else:
                max_num_groups = groups
    return max_num_groups


# Return the peak elements' indices in the given array A
def peak_idxs_in(A):
    peak_idxs = []
    for idx in range(1, len(A)-1):
        left = A[idx-1]
        cur = A[idx]
        right = A[idx+1]
        if cur > left and cur > right:
            peak_idxs.append(idx)
    return peak_idxs
