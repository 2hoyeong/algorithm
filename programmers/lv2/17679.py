# https://school.programmers.co.kr/learn/courses/30/lessons/17679
# 2018 KAKAO BLIND RECRUITMENT
# [1차] 프렌즈4블록

def solution(m, n, board):
    l_board = []
    answer = 0
    for b in board:
        l_board.append(list(b))

    while True:
        bomb = set()

        for i in range(m - 1):
            for j in range(n - 1):
                if l_board[i][j] != '#':
                    if l_board[i][j] == l_board[i + 1][j] == l_board[i][j + 1] == l_board[i + 1][j + 1]:
                        bomb.add((i, j))
                        bomb.add((i + 1, j))
                        bomb.add((i, j + 1))
                        bomb.add((i + 1, j + 1))
                                
        if len(bomb) == 0:
            break
        
        for b in bomb:
            l_board[b[0]][b[1]] = '#'
        
        clean(l_board)
        
        answer += len(bomb)

    return answer

def clean(board):
    for j in range(len(board[0])):
        for i in range(len(board) - 1, 0, -1):
            if board[i][j] == '#':
                for k in range(i - 1, -1, -1):
                    if board[k][j] != '#':
                        board[i][j] = board[k][j]
                        board[k][j] = '#'
                        break
