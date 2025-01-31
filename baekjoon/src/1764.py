import sys

N, M = map(int, input().split())

l = set()
for _ in range(N):
    name = sys.stdin.readline().rstrip()
    l.add(name)

result = []
for _ in range(M):
    name = sys.stdin.readline().rstrip()
    if name in l:
        result.append(name)
result.sort()

print(len(result))
for r in result:
    print(r)
