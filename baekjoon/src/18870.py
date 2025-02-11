import sys
N = int(input())

X = list(map(int, sys.stdin.readline().rstrip().split()))

sorted_x = sorted(set(X))
map_x = {}

for i in range(len(sorted_x)):
    if not sorted_x[i] in map_x:
        map_x[sorted_x[i]] = i

result = []
for x in X:
    result.append(str(map_x[x]))

print(' '.join(result))
