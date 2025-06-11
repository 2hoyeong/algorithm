# https://school.programmers.co.kr/learn/courses/30/lessons/49189
# 가장 먼 노드

from collections import deque

def solution(n, edge):
    board = {}
    distance = [-1] * (n + 1)
    for i in range(1, n + 1):
        board[i] = []
    
    for e in edge:
        a, b = e
        board[a].append(b)
        board[b].append(a)
    
    queue = deque()
    queue.append((1, 0))
    max_distance = 0
    while queue:
        now, depth = queue.pop()
        
        if distance[now] != -1:
            continue
            
        if max_distance < depth:
            max_distance = depth

        distance[now] = depth
        
        for e in board[now]:
            queue.appendleft((e, depth + 1))

    return distance.count(max_distance)
