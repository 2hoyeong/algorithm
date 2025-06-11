# https://school.programmers.co.kr/learn/courses/30/lessons/169199
# 리코쳇 로봇

from collections import deque

def find_xy(board, target):
    for i in range(len(board)):
        y = board[i].find(target)
        if y > -1:
            return [i, y]
    
    raise 'Not found'

def solution(board):
    
    r_xy = find_xy(board, 'R')
    g_xy = find_xy(board, 'G')
    for i in range(len(board)):
        board[i] = list(board[i])

    A, B = len(board), len(board[0])
    
    queue = deque()
    queue.append((r_xy[0], r_xy[1], 0))
    visited = [[False] * B for _ in range(A)]
    
    while queue:
        x, y, depth = queue.pop()
        
        if visited[x][y] == True:
            continue
            
        visited[x][y] = True
        
        if board[x][y] == 'G':
            return depth
        
        if x < A - 1 and board[x + 1][y] != 'D':
            to_x = go_down(board, x, y)
            queue.appendleft((to_x, y, depth + 1))
        if x > 0 and board[x - 1][y] != 'D':
            to_x = go_up(board, x, y)
            queue.appendleft((to_x, y, depth + 1))
        if y < B - 1 and board[x][y + 1] != 'D':
            to_y = go_right(board, x, y)
            queue.appendleft((x, to_y, depth + 1))
        if y > 0 and board[x][y - 1] != 'D':
            to_y = go_left(board, x, y)
            queue.appendleft((x, to_y, depth + 1))
        
    return -1

def go_down(board, x, y):
    down = len(board)
    end = x
    for i in range(x, down):
        if board[i][y] == 'D':
            break
        else:
            end = i

    return end

def go_up(board, x , y):
    end = x
    for i in range(x, -1, -1):
        if board[i][y] == 'D':
            break
        else:
            end = i
    return end

def go_right(board, x, y):
    right = len(board[x])
    end = y
    for i in range(y, right):
        if board[x][i] == 'D':
            break
        else:
            end = i
    
    return end

def go_left(board, x, y):
    end = y
    for i in range(y, -1, -1):
        if board[x][i] == 'D':
            break
        else:
            end = i

    return end
