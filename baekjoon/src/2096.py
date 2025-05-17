import sys

N = int(sys.stdin.readline().rstrip())

l, m, r = map(int, sys.stdin.readline().rstrip().split())
minimum = [l, m, r]
maximum = [l, m, r]

for _ in range(1, N):
    l, m, r = map(int, sys.stdin.readline().rstrip().split())
    min_0 = l + min(minimum[0], minimum[1])
    min_1 = m + min(minimum)
    min_2 = r + min(minimum[1], minimum[2])

    max_0 = l + max(maximum[0], maximum[1])
    max_1 = m + max(maximum)
    max_2 = r + max(maximum[1], maximum[2])
    minimum = [min_0, min_1, min_2]
    maximum = [max_0, max_1, max_2]

print(max(maximum), min(minimum))
