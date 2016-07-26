"""
Created by JeongMinCha on 2016. 7. 26.
"""
def solution(S, P, Q):
    minimal_factors = []

    prefix_A = [0] * (len(S)+1)
    prefix_C = [0] * (len(S)+1)
    prefix_G = [0] * (len(S)+1)
    prefix_T = [0] * (len(S)+1)

    # print(prefix_sum)
    for i in range(len(S)):
        a = 0; c = 0; g = 0; t = 0
        if S[i] == 'A': a = 1
        if S[i] == 'C': c = 1
        if S[i] == 'G': g = 1
        if S[i] == 'T': t = 1
        prefix_A[i + 1] = prefix_A[i] + a
        prefix_C[i + 1] = prefix_C[i] + c
        prefix_G[i + 1] = prefix_G[i] + g
        prefix_T[i + 1] = prefix_T[i] + t

    for i in range(len(P)):
        fromIdx = P[i]
        toIdx = Q[i] + 1
        if prefix_A[toIdx] - prefix_A[fromIdx] > 0:
            minimal_factors.append(1)
        elif prefix_C[toIdx] - prefix_C[fromIdx] > 0:
            minimal_factors.append(2)
        elif prefix_G[toIdx] - prefix_G[fromIdx] > 0:
            minimal_factors.append(3)
        elif prefix_T[toIdx] - prefix_T[fromIdx] > 0:
            minimal_factors.append(4)

    return minimal_factors