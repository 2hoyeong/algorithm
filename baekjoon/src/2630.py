N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
white, blue = 0, 0

def divide(x, y, n):
    global white, blue

    if n == 1:
        if board[x][y] == 1:
            blue += 1
        else:
            white += 1
    else:
        flag = board[x][y]
        all_same = True
        for xx in range(n):
            for yy in range(n):
                if board[x + xx][y + yy] != flag:
                    all_same = False
                    break
            if not all_same:
                break
        
        if all_same:
            if flag == 1:
                blue += 1
            else:
                white += 1
        else:
            n_size = n // 2

            divide(x, y, n_size)
            divide(x + n_size, y, n_size)
            divide(x, y + n_size, n_size)
            divide(x + n_size, y + n_size, n_size)

divide(0, 0, N)
print(white)
print(blue)
