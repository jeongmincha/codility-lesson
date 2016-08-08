"""
Created by JeongMinCha on 2016. 8. 9.
"""


def fibonacciDynamic(n):
    """
    Finding Fibonacci numbers dynamically.
    :param n: input number n
    :return: fibonacci number of given n
    """
    fib = [0] * (n+2)
    fib[1] = 1
    for i in xrange(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]