"""
Created by JeongMinCha on 2016. 8. 9.
"""


def fibonacci(n):
    """
    Finding Fibonacci numbers recursively.
    :param n: input number n
    :return: fibonacci number of given n
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)