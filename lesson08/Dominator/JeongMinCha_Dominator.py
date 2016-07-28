"""
Created by JeongMinCha on 2016. 7. 29.
"""
def solution(A):
    cnt_dict = {}
    idx_dict = {}

    for (idx, a) in enumerate(A):
        if a not in cnt_dict:
            cnt_dict[a] = 1
            idx_dict[a] = [idx]
        else:
            cnt_dict[a] += 1
            idx_dict[a].append(idx)

    for val in cnt_dict.keys():
        if cnt_dict[val] > len(A) / 2:
            return idx_dict[val][0]

    return -1
