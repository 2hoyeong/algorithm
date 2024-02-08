# https://school.programmers.co.kr/learn/courses/30/lessons/161989
# 덧칠하기

def solution(n, m, section):
    answer = 1
    p = section[0]
    for s in section[1:]:
        if s - p < m:
            continue
        p = s
        answer += 1
            
    
    return answer
