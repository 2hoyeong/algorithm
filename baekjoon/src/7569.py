from collections import deque

M, N, H = map(int, input().split())

tomato = []
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

for i in range(H):
  tomato.append([])
  for _ in range(N):
      tomato[i].append(list(map(int, input().split())))

queue = deque()
for k in range(H):
  for i in range(N):
      for j in range(M):
          if tomato[k][i][j] == 1:
              queue.appendleft((k, i, j))

while queue:
    z, x, y = queue.pop()
    if x < 0 or x >= N or y < 0 or y >= M or z < 0 or z >= H:
        continue
    if tomato[z][x][y] != -1 and visited[z][x][y] == False:
        visited[z][x][y] = True
        if y + 1 < M:
            if tomato[z][x][y + 1] == 0:
                tomato[z][x][y + 1] = tomato[z][x][y] + 1
            else:
                tomato[z][x][y + 1] = min(tomato[z][x][y + 1], tomato[z][x][y] + 1)
            queue.appendleft((z, x, y + 1))
        if y - 1 >= 0:
            if tomato[z][x][y - 1] == 0:
                tomato[z][x][y - 1] = tomato[z][x][y] + 1
            else:
                tomato[z][x][y - 1] = min(tomato[z][x][y - 1], tomato[z][x][y] + 1)
            queue.appendleft((z, x, y - 1))
        if x + 1 < N:
            if tomato[z][x + 1][y] == 0:
                tomato[z][x + 1][y] = tomato[z][x][y] + 1
            else:
                tomato[z][x + 1][y] = min(tomato[z][x + 1][y], tomato[z][x][y] + 1)
            queue.appendleft((z, x + 1, y))
        if x - 1 >= 0:
            if tomato[z][x - 1][y] == 0:
                tomato[z][x - 1][y] = tomato[z][x][y] + 1
            else:
                tomato[z][x - 1][y] = min(tomato[z][x - 1][y], tomato[z][x][y] + 1)
            queue.appendleft((z, x - 1, y))
        if z + 1 < H:
            if tomato[z + 1][x][y] == 0:
                tomato[z + 1][x][y] = tomato[z][x][y] + 1
            else:
                tomato[z + 1][x][y] = min(tomato[z + 1][x][y], tomato[z][x][y] + 1)
            queue.appendleft((z + 1, x, y))
        if z - 1 >= 0:
            if tomato[z - 1][x][y] == 0:
                tomato[z - 1][x][y] = tomato[z][x][y] + 1
            else:
                tomato[z - 1][x][y] = min(tomato[z - 1][x][y], tomato[z][x][y] + 1)
            queue.appendleft((z - 1, x, y))
no_tomato = False

for k in range(H):
  for i in range(N):
      for j in range(M):
          if visited[k][i][j] == False and tomato[k][i][j] != -1:
              no_tomato = True
              break

if no_tomato:
    print('-1')
else:
    print(max(max(max(row) for row in layer) for layer in tomato) - 1)
