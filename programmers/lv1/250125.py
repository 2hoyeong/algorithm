# https://school.programmers.co.kr/learn/courses/30/lessons/250125
# PCCE 기출문제
# 이웃한 칸

def solution(board, h, w):
    answer = 0
    color = board[h][w]
    l = len(board)
    if h > 0 and board[h - 1][w] == color:
        answer += 1
    if h < l - 1 and board[h + 1][w] == color:
        answer += 1
    if w > 0 and board[h][w - 1] == color:
        answer += 1
    if w < l - 1 and board[h][w + 1] == color:
        answer += 1

    return answer
