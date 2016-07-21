def solution(A):
    if len(A) == 1 and A[0] == 1:
        return 2

    unique_list = sorted(set(A))
    unique_list = [x for x in unique_list if x > 0]

    if len(unique_list) == 0:
        return 1

    c = 1
    for e in unique_list:
        if e is not c:
            return c
        c += 1

    return unique_list[0] - 1