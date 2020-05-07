# https://programmers.co.kr/learn/courses/30/lessons/17682
# 다트 게임
# 2018 KAKAO BLIND RECRUITMENT

import re

def solution(dartResult):
    b = {'S' : 1, 'D' : 2, 'T' : 3}
    o = {'' : 1, '*' : 2, '#' : -1}
    regex = re.compile("(\d+)([SDT])([*|#]?)")
    score = regex.findall(dartResult)
    for i, v in enumerate(score):
        point = v[0]
        bonus = v[1]
        option = v[2]
        if option == '*' and i > 0:
            score[i - 1] *= 2
        score[i] = int(point) ** b[bonus] * o[option]

    return sum(score)