# https://programmers.co.kr/learn/courses/30/lessons/42839
# 소수 찾기

import itertools

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    per = set()
    for i in range(len(numbers)):
        number = set(itertools.permutations(numbers, i + 1))
        for n in number:
            per.add(int(''.join(n)))
    for p in per:
        if p > 1:
            if isPN(p):
                answer += 1
    return answer

def isPN(number):
    if number > 1:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True
    return False
