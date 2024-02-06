# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# 귤 고르기

def solution(k, tangerine):
    t = {}
    for s in tangerine:
        if s in t:
            t[s] += 1
        else:
            t[s] = 1
    
    v = sorted(t.values(), reverse=True)
    answer = 0
    for mv in v:
        answer += 1
        k -= mv
        if k <= 0:
            break

    return answer
