# https://programmers.co.kr/learn/courses/30/lessons/43105
# 정수 삼각형

def solution(triangle):
    for i, side in enumerate(triangle[:-1]):
        for s in range(len(side)):
            if s == 0:
                triangle[i + 1][s] += triangle[i][s]
            if s == len(side) - 1:
                triangle[i + 1][s + 1] += triangle[i][s]
            else:
                triangle[i + 1][s + 1] += max(triangle[i][s], triangle[i][s + 1])
    
    return max(triangle[-1])