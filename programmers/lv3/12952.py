# https://programmers.co.kr/learn/courses/30/lessons/12952
# N-Queen

def canNotAttack(queen, location):
    for i in range(len(queen)):
        if queen[i] == -1:
            continue
        if abs(i - location[0]) == abs(queen[i] - location[1]):
            return False
    return True

def dfs_queen(row, n, queen):
    if row == n:
        queen[queen.index(row - 1)] = -1
        return 1
    answer = 0
    for i in range(n):
        if queen[i] != -1:
            continue
        if canNotAttack(queen, [i, row]):
            queen[i] = row
            answer += dfs_queen(row + 1, n, queen)
    if queen:
        queen[queen.index(row - 1)] = -1
    return answer

def solution(n):
    return dfs_queen(0, n, [-1] * n)