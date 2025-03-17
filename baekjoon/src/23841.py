N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))

for i in range(N):
    for j in range(M // 2):
      if board[i][j] != '.':
         board[i][M - j - 1] = board[i][j]
      else:
         board[i][j] = board[i][M - j - 1]

for i in range(N):
    print(''.join(board[i]))
