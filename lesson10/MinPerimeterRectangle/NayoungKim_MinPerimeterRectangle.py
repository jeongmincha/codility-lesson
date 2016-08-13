def solution(N):
    i = 1
    P = []
    
    while i * i < N:
        if N % i == 0:
            P.append(2*(i+(N/i)))
        i += 1
    if i * i == N:
        P.append(4*i)
    
    return P[-1]