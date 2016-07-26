"""
Created by JeongMinCha on 2016. 7. 26.
"""
def solution(S, P, Q):
    minimal_factors = []
    impact = dict({'A':1, 'C':2, 'G': 3, 'T': 4})

    for idx in range(len(P)):
        mn = min([impact[S[idx]] for idx in range(P[idx], Q[idx]+1)])
        minimal_factors.append(mn)

    return minimal_factors