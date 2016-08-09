"""
Created by JeongMinCha on 2016. 8. 9.
"""


def solution(A, B):
    res = [0] * len(A)
    max_mod = (1 << max(B)) - 1
    fib = fibonacci(max(A), max_mod)

    for idx in xrange(len(A)):
        a = A[idx]
        b = B[idx]
        res[idx] = fib[a+1] & ((1 << b) - 1)
    return res


def fibonacci(N, max_mod):
    fib = [0] * (N+2)
    fib[1] = 1
    for i in xrange(2, N+2):
        fib[i] = (fib[i-1] + fib[i-2]) & max_mod
    return fib
