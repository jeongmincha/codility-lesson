"""
Created by JeongMinCha on 2016. 7. 29.
"""
def solution(A):
    candidate = -1
    candidate_cnt = 0

    for idx in range(0, len(A)):
        if candidate_cnt == 0:
            candidate = A[idx]
            candidate_cnt += 1
        else:
            if A[idx] == candidate:
                candidate_cnt += 1
            else:
                candidate_cnt -= 1

    leader_count = len([number for number in A if number == candidate])
    if leader_count <= len(A) / 2:
        return 0
    else:
        leader = candidate

    equi_leaders = 0
    front_leader_cnt = 0
    for idx in range(0, len(A)):
        if A[idx] == leader:
            front_leader_cnt += 1
        if front_leader_cnt > (idx+1) / 2 and \
           leader_count-front_leader_cnt > (len(A) - (idx+1)) / 2:
            equi_leaders += 1

    return equi_leaders
