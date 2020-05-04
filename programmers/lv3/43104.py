# https://programmers.co.kr/learn/courses/30/lessons/43104
# 타일 장식물
# 

def solution(N):
    sq = [1, 1]
    for i in range(2, N):
        sq.append(sq[i - 2] + sq[i - 1])
    return (sq[-2] + sq[-1] + sq[-1]) * 2