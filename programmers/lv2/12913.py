# https://school.programmers.co.kr/learn/courses/30/lessons/12913
# 땅따먹기

def solution(land):
    for i, g in enumerate(land[1:]):
        for j in range(len(g)):
            next_g = [element for k, element in enumerate(land[i]) if k != j]
            land[i + 1][j] += max(next_g)

    return max(land[-1])
