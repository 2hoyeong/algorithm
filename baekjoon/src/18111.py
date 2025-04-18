N ,M, B = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

max_height = 0
min_time = 128000001
for h in range(257):
    b = B
    time = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > h:
                time += (board[i][j] - h) * 2
                b += (board[i][j] - h)
            else:
                time += h - board[i][j]
                b -= (h - board[i][j])
                

    if min_time >= time and b >= 0:
        min_time = time
        max_height = h

print(min_time, max_height)
