# https://programmers.co.kr/learn/courses/30/lessons/42898
# 등굣길

def solution(m, n, puddles):
    way = [[0] * (m + 1) for _ in range(n + 1)]
    way[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [j, i] in puddles:
                way[i][j] = 0
            else:
                way[i][j] += way[i - 1][j] + way[i][j - 1]
    return way[n][m] % 1000000007