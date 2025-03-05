from collections import deque

M, N = map(int, input().split())
board = []
visited = [[False] * N for _ in range(M)]
for _ in range(M):
    board.append(list(map(int, list(input()))))

queue = deque()
queue.append([0, 0, 1])

while queue:
    x, y, move = queue.pop()

    if visited[x][y] == True:
        continue
    
    if board[x][y] == 0:
        continue
    
    if x == M - 1 and y == N - 1:
        print(move)
        break
    
    visited[x][y] = True
    
    if x + 1 < M:
        queue.appendleft(([x + 1, y, move + 1]))
    if x - 1 >= 0:
        queue.appendleft(([x - 1, y, move + 1]))
    if y + 1 < N:
        queue.appendleft(([x, y + 1, move + 1]))
    if y - 1 >= 0:
        queue.appendleft(([x, y - 1, move + 1]))
