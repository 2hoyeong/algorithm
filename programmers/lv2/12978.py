# https://school.programmers.co.kr/learn/courses/30/lessons/12978
# Summer/Winter Coding(~2018)
# 배달

from collections import deque

def solution(N, road, K):
    board = [[10001] * N for _ in range(N)]
    result = [500001] * N
    
    for r in road:
        f, t, d = r
        if board[f - 1][t - 1] > d:
            board[f - 1][t - 1] = d
            board[t - 1][f - 1] = d

    queue = deque()
    queue.append(0)
    result[0] = 0
    
    while queue:
        now = queue.pop()
        
        for i in range(N):
            if board[now][i] != 10001:
                if result[i] > result[now] + board[now][i]:
                    result[i] = result[now] + board[now][i]
                    queue.appendleft(i)

    answer = 0
    for r in result:
        if r <= K:
            answer += 1
        
    return answer
