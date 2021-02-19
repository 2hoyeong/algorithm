# https://programmers.co.kr/learn/courses/30/lessons/64065
# 2019 카카오 개발자 겨울 인턴십
# 튜플

import re

def solution(s):
    s = s[2:-2].split("},{")
    answer = []
    for c in sorted(s, key= lambda x : len(x)):
        for tuple in c.split(","):
            if tuple not in answer:
                answer.append(tuple)
    return list(map(int, answer))