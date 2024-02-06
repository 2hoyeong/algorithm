# https://school.programmers.co.kr/learn/courses/30/lessons/131705
# 삼총사

from itertools import combinations

def solution(number):
    sam = combinations(number, 3)
    answer = 0
    for three in sam:
        if sum(three) == 0:
            answer += 1
    return answer
