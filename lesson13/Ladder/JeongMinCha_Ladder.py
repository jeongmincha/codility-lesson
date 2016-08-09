"""
Created by JeongMinCha on 2016. 8. 9.
"""


def solution(A, B):
    res = list()
    for idx in xrange(len(A)):
        a = A[idx]
        b = B[idx]
        res.append(fibonacci(a+1) % pow(2, b))
    return res


def fibonacci(N):
    fib = [0] * (N+2)
    fib[1] = 1
    for i in xrange(2, N+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[N]
