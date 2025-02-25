import sys
from collections import deque

Y, X = map(int, sys.stdin.readline().rstrip().split())

board = []
visited = [[False] * X for _ in range(Y)]

start_point = [0, 0]

for i in range(Y):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    try:
        j = row.index(2)
        start_point = [i, j]
    except:
        pass
    board.append(row)

queue = deque()
queue.append((start_point, -1))

while queue:
    now, dis = queue.pop()
    y, x = now
    if visited[y][x] or board[y][x] == 0:
        continue
    
    visited[y][x] = True
    board[y][x] = dis + 1
    if x + 1 < X:
        queue.appendleft(([y, x + 1], dis + 1))
    if x - 1 >= 0:
        queue.appendleft(([y, x - 1], dis + 1))
    if y + 1 < Y:
        queue.appendleft(([y + 1, x], dis + 1))
    if y - 1 >= 0:
        queue.appendleft(([y - 1, x], dis + 1))

for y in range(Y):
    for x in range(X):
        if visited[y][x] == False and board[y][x] == 1:
            print(-1, end=' ')
        else:
            print(board[y][x], end=' ')
    print()
