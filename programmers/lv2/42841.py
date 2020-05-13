# https://programmers.co.kr/learn/courses/30/lessons/42841
# 숫자 야구

import itertools

def solution(baseball):
    answer = []
    numbers = list(itertools.permutations(list(range(1, 10)), 3))
    for number in numbers:
        isCandidate = False
        for n, s, b in baseball:
            n = str(n)
            strike = 0
            ball = 0
            for i in range(3):
                if int(n[i]) == number[i]:
                    strike += 1
                elif int(n[i]) in number:
                    ball += 1
            if s == strike and b == ball:
                isCandidate = True
            else:
                isCandidate = False
                break
        
        if isCandidate:
            answer.append(number)

    return len(answer)
	