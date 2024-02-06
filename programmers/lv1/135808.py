# https://school.programmers.co.kr/learn/courses/30/lessons/135808
# 과일 장수

def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    index = 0
    while len(score) > index:
        if len(score) - index < m:
            break
        index += m
        answer += score[index - 1] * m
    return answer
