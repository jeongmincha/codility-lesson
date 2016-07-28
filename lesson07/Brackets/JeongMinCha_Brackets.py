"""
Created by JeongMinCha on 2016. 7. 29.
"""
def solution(S):
    stack = []
    map = {
        '{':'}',
        '[':']',
        '(':')'
    }

    for s in S:
        if s in map.keys():
            stack.append(s)
        else:
            if len(stack) == 0:
                return 0
            elif s == map[stack[-1]]:
                stack.pop()
            else:
                return 0

    if len(stack) == 0:
        return 1
    else:
        return 0