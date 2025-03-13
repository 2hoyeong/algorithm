N, M = map(int, input().split())

answer = []

def dfs(acc, start):
    if len(acc) == M:
        answer.append(acc)
        return

    for i in range(start, N + 1):
        dfs(acc + str(i), i)

dfs("", 1)
for a in answer:
    print(" ".join(list(a)))
