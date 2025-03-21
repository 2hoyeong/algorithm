N, M = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()
answer = []
visited = [False] * N

def dfs(acc):
    if len(acc) == M:
        answer.append(acc)
        return

    for i in range(N):
        if visited[i] == False:
            visited[i] = True
            acc.append(str(nums[i]))
            dfs(acc.copy())
            acc.pop()
            visited[i] = False

dfs([])
dups = set()
for a in answer:
    output = " ".join(a)
    if output not in dups:
        dups.add(output)
        print(output)
