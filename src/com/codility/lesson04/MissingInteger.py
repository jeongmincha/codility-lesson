def solution(A):
    unique_list = sorted(set(A))

    last = 0
    for e in unique_list:
        if e is not last+1:
            return last+1
        last += 1
    return -1