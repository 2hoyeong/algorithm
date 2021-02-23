# https://programmers.co.kr/learn/courses/30/lessons/70128
# 월간 코드 챌린지 시즌1
# 내적

def solution(a, b):
    answer = 0
    for i in zip(a, b):
        answer += i[0] * i[1]
    return answer