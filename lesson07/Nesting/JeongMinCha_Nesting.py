"""
Created by JeongMinCha on 2016. 7. 29.
"""
def solution(S):
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
            else:
                stack.pop()
    if len(stack) == 0:
        return 1
    else:
        return 0