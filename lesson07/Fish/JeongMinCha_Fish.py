"""
Created by JeongMinCha on 2016. 7. 28.
"""
def solution(A, B):
    num_alive_fishs = 0
    downstream_fishs = []
    DOWNSTREAM = 1

    for idx in range(0, len(A)):
        fish_size = A[idx]
        direction = B[idx]

        if direction is DOWNSTREAM:
            downstream_fishs.append(A[idx])
        else:
            while len(downstream_fishs) is not 0:
                if fish_size > downstream_fishs[-1]:
                    downstream_fishs.pop()
                else:
                    break
            else:
                num_alive_fishs += 1

    num_alive_fishs += len(downstream_fishs)

    return num_alive_fishs