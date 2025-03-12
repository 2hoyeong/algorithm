N, M = map(int, input().split())

answer = []
visited = [False] * (N + 1)

def dfs(acc, start):
    if len(acc) == M:
        answer.append(acc)
        return

    for i in range(start, N + 1):
        if visited[i] == False:
            visited[i] = True
            dfs(acc + str(i), i)
            visited[i] = False

dfs("", 1)
for a in answer:
    print(" ".join(list(a)))
