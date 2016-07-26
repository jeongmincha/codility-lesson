"""
Created by JeongMinCha on 2016. 7. 21.
"""
def solution(A):
    if len(A) == 1 and A[0] == 1:
        return 2

    unique_list = sorted(set(A))
    unique_list = [x for x in unique_list if x > 0]

    if len(unique_list) == 0:
        return 1

    perm = True
    c = 1
    for e in unique_list:
        if e != c:
            perm = False
            return c
        c += 1

    if perm is True and unique_list[0] == 1:
        return unique_list[len(unique_list)-1] + 1

    return unique_list[0] - 1