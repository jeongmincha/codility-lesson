"""
Created by JeongMinCha on 2016. 8. 9.
"""


def fibonacci(n):
    """
    Finding Fibonacci numbers recursively.
    This algorithm performs Fn additions of 1, and,
    as the sequence grows exponentially, we get an
    inefficient solution.
    :param n: input number n
    :return: fibonacci number of given n
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)