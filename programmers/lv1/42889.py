# https://programmers.co.kr/learn/courses/30/lessons/42889
# 실패율
# 2019 KAKAO BLIND RECRUITMENT

def solution(N, stages):
    fail = {}
    try_p = len(stages)
    for stage in range(1, N + 1):
        fail_p = stages.count(stage)
        if try_p == 0:
            fail[stage] = 0
        else:
            fail[stage] = fail_p / try_p   
        try_p -= fail_p
    return sorted(fail, key=lambda l : fail[l], reverse=True)