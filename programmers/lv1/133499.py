# https://school.programmers.co.kr/learn/courses/30/lessons/133499
# 옹알이 (2)

import re

def solution(babbling):
    joka = {"aya": "!", "ye": "@", "woo": "#", "ma": "$"}
    rg = re.compile('^[!@#$]+$')
    answer = 0
    for bb in babbling:
        b = bb
        for j, r in joka.items():
            b = b.replace(j, r)

        if rg.match(b) and checkdup(b):
            answer += 1
    return answer

def checkdup(b):
    t = b[0]
    for c in b[1:]:
        if t == c:
            return False
        t = c
    return True
