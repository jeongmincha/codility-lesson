"""
Created by JeongMinCha on 2016. 8. 4.
"""
def solution(A, B):
    pairs = 0
    for idx in range(len(A)):
        if has_same_factors(A[idx], B[idx]):
            pairs += 1
    return pairs

def has_same_factors(a, b):
    g = gcd(a, b)

    while a != 1:
        a_gcd = gcd(a, g)
        if a_gcd == 1:
            break
        a /= a_gcd
    else:
        while b != 1:
            b_gcd = gcd(b, g)
            if b_gcd == 1:
                break
            b /= b_gcd
        else:
            return True

    return False

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)