"""
Created by JeongMinCha on 2016. 7. 29.
"""
def solution(H):
    stones = 0
    stack = []

    for h in H:
        while len(stack) > 0 and h < stack[-1]:
            stack.pop()
        if len(stack) > 0 and h == stack[-1]:
            continue
        else:
            stones += 1
            stack.append(h)

    return stones