# https://school.programmers.co.kr/learn/courses/30/lessons/340198
# PCCP 기출문제
# 공원

def solution(mats, park):
    answer = -1
    mats.sort(reverse=True)

    maximumEmpty = -1
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] != "-1":
                continue
            maximumEmpty = max(maximumEmpty, getMaxSize(i, j, park))
    
    for mat in mats:
        if mat <= maximumEmpty:
            answer = mat
            break        

    return answer

def getMaxSize(i, j, park):
    depth = 1
    while True:
        if i + depth >= len(park) or j + depth >= len(park[i]):
            break
        
        for x in range(i, i + depth + 1):
            for y in range(j, j + depth + 1):
                if park[x][y] != "-1":
                    return depth
        
        depth += 1
    
    return depth
