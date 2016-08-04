"""
Created by JeongMinCha on 2016. 8. 4.
"""
def solution(N, M):
    lcm = N * M / gcd(N, M)
    return lcm / M

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
