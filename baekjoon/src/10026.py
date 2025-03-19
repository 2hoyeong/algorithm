N = int(input())
board = []

for _ in range(N):
    board.append(list(input()))

n1 = 0
visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            stack = [[i, j]]
            n1 += 1
            while stack:
                x, y = stack.pop()
                if visited[x][y] == True or board[x][y] != board[i][j]:
                    continue
                visited[x][y] = True
                if x - 1 >= 0:
                    stack.append([x - 1, y])
                if x + 1 < N:
                    stack.append([x + 1, y])
                if y - 1 >= 0:
                    stack.append([x, y - 1])
                if y + 1 < N:
                    stack.append([x, y + 1])

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == "R":
            board[i][j] = "G"

n2 = 0

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            stack = [[i, j]]
            n2 += 1
            while stack:
                x, y = stack.pop()
                if visited[x][y] == True or board[x][y] != board[i][j]:
                    continue
                visited[x][y] = True
                if x - 1 >= 0:
                    stack.append([x - 1, y])
                if x + 1 < N:
                    stack.append([x + 1, y])
                if y - 1 >= 0:
                    stack.append([x, y - 1])
                if y + 1 < N:
                    stack.append([x, y + 1])

print(n1, n2)
