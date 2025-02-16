from collections import deque

M, N = map(int, input().split())

tomato = []
visited = [[False] * M for _ in range(N)]
for _ in range(N):
    tomato.append(list(map(int, input().split())))

queue = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.appendleft((i, j))

while queue:
    x, y = queue.pop()
    if x < 0 or x >= N or y < 0 or y >= M:
        continue
    if tomato[x][y] != -1 and visited[x][y] == False:
        visited[x][y] = True
        if y + 1 < M:
            if tomato[x][y + 1] == 0:
                tomato[x][y + 1] = tomato[x][y] + 1
            else:
                tomato[x][y + 1] = min(tomato[x][y + 1], tomato[x][y] + 1)
            queue.appendleft((x, y + 1))
        if y - 1 >= 0:
            if tomato[x][y - 1] == 0:
                tomato[x][y - 1] = tomato[x][y] + 1
            else:
                tomato[x][y - 1] = min(tomato[x][y - 1], tomato[x][y] + 1)
            queue.appendleft((x, y - 1))
        if x + 1 < N:
            if tomato[x + 1][y] == 0:
                tomato[x + 1][y] = tomato[x][y] + 1
            else:
                tomato[x + 1][y] = min(tomato[x + 1][y], tomato[x][y] + 1)
            queue.appendleft((x + 1, y))
        if x - 1 >= 0:
            if tomato[x - 1][y] == 0:
                tomato[x - 1][y] = tomato[x][y] + 1
            else:
                tomato[x - 1][y] = min(tomato[x - 1][y], tomato[x][y] + 1)
            queue.appendleft((x - 1, y))
no_tomato = False

for i in range(N):
    for j in range(M):
        if visited[i][j] == False and tomato[i][j] != -1:
            no_tomato = True
            break

if no_tomato:
    print('-1')
else:
    print(max(max(row) for row in tomato) - 1)
