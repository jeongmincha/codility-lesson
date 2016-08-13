"""
Created by JeongMinCha on 2016. 8. 10.
"""


def solution(K, M, A):
    beg = max(A)
    end = sum(A)

    if K == 1:
        return end
    if K >= len(A):
        return beg

    while beg <= end:
        mid = (beg + end) / 2
        if block_size_is_valid(A, K, mid):
            end = mid - 1
        else:
            beg = mid + 1

    return beg


def block_size_is_valid(A, max_block_num, max_block_sum):
    block_sum = 0
    block_cnt = 0

    last = -1
    for element in A:
        if block_sum + element > max_block_sum:
            block_sum = element
            block_cnt += 1
        else:
            block_sum += element
        if block_cnt >= max_block_num:
            return False
    return True