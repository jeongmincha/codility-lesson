def solution(N):
    i = 1
    num = 0
    while i * i < N:
        if N % i == 0:
            num += 2
        i += 1
    if i * i == N:
        num += 1
        
    return num