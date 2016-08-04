"""
Created by JeongMinCha on 2016. 8. 4.
"""
import math

def solution(A):
    mx = max(A)

    # key = element, value = occurences of the number
    count = {}
    for elem in A:
        count[elem] = count.get(elem, 0) + 1

    # key = element, value = list of divisors of the number
    divisors = {}
    for elem in A:
        divisors[elem] = [1]

    # find all divisors
    for divisor in range(2, int(math.sqrt(mx)) + 1):
        multiple = divisor
        while multiple <= mx:
            if multiple in divisors and not divisor in divisors[multiple]:
                divisors[multiple].append(divisor)
            multiple += divisor

    # find all quotients as divisors
    for elem in divisors:
        quotients = [elem/div for div in divisors[elem]]
        quotients = [quot for quot in quotients if quot not in divisors[elem]]
        divisors[elem].extend(quotients)

    # calculate number of non-divisors of each elements.
    result = []
    for elem in A:
        num_divisors = sum([count.get(div, 0) for div in divisors[elem]])
        result.append(len(A) - num_divisors)

    return result