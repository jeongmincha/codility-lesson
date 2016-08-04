"""
Created by JeongMinCha on 2016. 8. 4.
"""
def solution(N, M):
    chocolates = [True] * N
    chocolates[0] = False

    num_eating = 1
    pos = M

    while chocolates[pos%N] == True:
        chocolates[pos%N] = False
        pos += M
        num_eating += 1

    return num_eating
