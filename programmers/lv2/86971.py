# https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 전력망을 둘로 나누기

def solution(n, wires):
    answer = 100
    for i in range(n - 1):
        board = [[0] * (n + 1) for _ in range(n + 1)]
        visited = [False] * (n + 1)
        
        for j in range(n - 1):
            if i == j:
                continue
            v1, v2 = wires[j]
            board[v1][v2] = 1
            board[v2][v1] = 1
            
        counts = []
        for j in range(1, n + 1):
            stack = []
            if visited[j] == False:
                stack.append(j)
                count = 0
                while stack:
                    x = stack.pop()
                    if visited[x] == True:
                        continue

                    visited[x] = True
                    count += 1
                    for l in range(n + 1):
                        if board[x][l] == 1:
                            stack.append(l)

                counts.append(count)
        answer = min(answer, abs(counts[0] - counts[1]))
    return answer
