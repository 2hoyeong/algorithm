# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 게임 맵 최단거리

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _ in range(n)]
    q = deque([[0, 0]])
    visited[0][0] = 1

    while len(q) > 0:
        now = q.popleft()
        x, y = now
        
        if y - 1 >= 0 and visited[x][y - 1] == 0 and maps[x][y - 1] == 1:
            q.append((x, y - 1))
            visited[x][y - 1] = visited[x][y] + 1
        if x - 1 >= 0 and visited[x - 1][y] == 0 and maps[x - 1][y] == 1:
            q.append((x - 1, y))
            visited[x - 1][y] = visited[x][y] + 1
        if y + 1 < m and visited[x][y + 1] == 0 and maps[x][y + 1] == 1:
            q.append((x, y + 1))
            visited[x][y + 1] = visited[x][y] + 1
        if x + 1 < n and visited[x + 1][y] == 0 and maps[x + 1][y] == 1:
            q.append((x + 1, y))
            visited[x + 1][y] = visited[x][y] + 1

    if visited[n - 1][m - 1] == 0:
        return -1
    return visited[n - 1][m - 1]
