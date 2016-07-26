"""
Created by JeongMinCha on 2016. 7. 26.
"""
def solution(N, A):
    counter = [0] * N
    current_max = 0 # The used value in previous max counter operation
    max_counter = 0 # The current max value

    for e in A:
        # increase(X) operation
        if 1 <= e <= N:
            # lazy write
            if max_counter > counter[e-1]:
                counter[e-1] = max_counter
            counter[e-1] += 1
            # max value update
            if current_max < counter[e-1]:
                current_max = counter[e-1]
        # max counter operation
        elif e == N+1:
            max_counter = current_max

    for i in range(len(counter)):
        if counter[i] < max_counter:
            counter[i] = max_counter

    return counter