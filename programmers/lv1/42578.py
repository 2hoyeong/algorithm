# https://programmers.co.kr/learn/courses/30/lessons/42578
# 위장

def solution(clothes):
    spy = {}
    for name, typ in clothes:
        if typ not in spy:
            spy[typ] = 0
        spy[typ] += 1
    answer = 1
    for s in spy.values():
        answer *= (s + 1)
    return answer - 1