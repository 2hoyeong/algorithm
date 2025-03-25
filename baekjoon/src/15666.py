N, M = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()
answer = []

def dfs(acc, j):
    if len(acc) == M:
        answer.append(acc)
        return

    for i in range(j, N):
        acc.append(str(nums[i]))
        dfs(acc.copy(), i)
        acc.pop()

dfs([], 0)
dups = set()
for a in answer:
    output = " ".join(a)
    if output not in dups:
        dups.add(output)
        print(output)
