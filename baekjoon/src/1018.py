H, W = map(int, input().split())

board = []
for _ in range(H):
    row = input()
    board.append(row)

def toggle(wb):
    if wb == "W":
        return "B"
    else:
        return "W"

def calcRePaint(start_x, start_y):
    kan = board[start_x][start_y]
    count = 0
    for x in range(start_x, start_x + 8):
        for y in range(start_y, start_y + 8):
            if board[x][y] != kan:
                count += 1
            kan = toggle(kan)
        kan = toggle(kan)
    
    kan = toggle(board[start_x][start_y])
    countNE = 0
    for x in range(start_x, start_x + 8):
        for y in range(start_y, start_y + 8):
            if board[x][y] != kan:
                countNE += 1
            kan = toggle(kan)
        kan = toggle(kan)

    return min(count, countNE)

answers = []
for w in range(W - 7):
    for h in range(H - 7):
        answers.append(calcRePaint(h, w))

print(min(answers))
