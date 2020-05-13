# https://programmers.co.kr/learn/courses/30/lessons/12924
# 숫자의 표현

def solution(n):
    answer = 1
    for i in range(n):
        s = 0
        while s < n:
            s += i
            i += 1
        if s == n:
            answer += 1
        
    return answer