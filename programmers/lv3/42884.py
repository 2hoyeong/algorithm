# https://programmers.co.kr/learn/courses/30/lessons/42884
# 단속카메라

def solution(routes):
    answer = []
    routes.sort(key= lambda x : (x[0], x[1]))
    out = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > out:
            answer.append(i)
            out = routes[i][1]
        else:
            out = min(routes[i][1], out)
    if answer[-1] != len(routes):
        return len(answer)+1
    return len(answer)