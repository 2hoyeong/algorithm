# https://programmers.co.kr/learn/courses/30/lessons/12982
# 예산
# Summer/Winter Coding(~2018)

def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        if budget - d[i] < 0:
            return i
        budget -= d[i]
    return i + 1