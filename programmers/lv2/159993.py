# https://school.programmers.co.kr/learn/courses/30/lessons/159993
# 미로 탈출

from collections import deque

def find_xy(maps, endpoint):
    xy = [0, 0]
    for i, row in enumerate(maps):
        idx = row.find(endpoint)
        if idx > -1:
            xy = [i, idx]
            break
    return xy

def solution(maps):
    answer = 0
    start_xy = find_xy(maps, 'S')
    lever_xy = find_xy(maps, 'L')
    end_xy = find_xy(maps, 'E')

    A, B = len(maps), len(maps[0])
    
    queue = deque()
    queue.append((start_xy[0], start_xy[1], 0))
    visited = [[False] * B for _ in range(A)]
    while queue:
        x, y, second = queue.pop()
        
        if visited[x][y] or maps[x][y] == 'X':
            continue
        
        visited[x][y] = True
        
        if x == lever_xy[0] and y == lever_xy[1]:
            answer = second
            break
        
        if x < A - 1:
            queue.appendleft((x + 1, y, second + 1))
        if x > 0:
            queue.appendleft((x - 1, y, second + 1))
        if y < B - 1:
            queue.appendleft((x, y + 1, second + 1))
        if y > 0:
            queue.appendleft((x, y - 1, second + 1))
    
    if answer == 0:
        return -1
    
    to_end = 0
    queue = deque()
    queue.append((lever_xy[0], lever_xy[1], 0))
    visited = [[False] * B for _ in range(A)]
    while queue:
        x, y, second = queue.pop()
        
        if visited[x][y] or maps[x][y] == 'X':
            continue
        
        visited[x][y] = True
        
        if x == end_xy[0] and y == end_xy[1]:
            to_end = second
            break
        
        if x < A - 1:
            queue.appendleft((x + 1, y, second + 1))
        if x > 0:
            queue.appendleft((x - 1, y, second + 1))
        if y < B - 1:
            queue.appendleft((x, y + 1, second + 1))
        if y > 0:
            queue.appendleft((x, y - 1, second + 1))

    if to_end == 0:
        return -1

    return answer + to_end
