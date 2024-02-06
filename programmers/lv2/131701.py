# https://school.programmers.co.kr/learn/courses/30/lessons/131701
# 연속 부분 수열 합의 개수

from itertools import permutations

def solution(elements):
    s = set()
    s.add(sum(elements))
    for e in elements:
        s.add(e)
    answer = 0
    for i in range(1, len(elements) - 1):
        l = elements + (elements[:i])
        for j in range(0, len(l) - i):
            s.add(sum(l[j:j+i+1]))
    return len(s)
