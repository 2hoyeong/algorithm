# 1, 2, 3 더하기
import sys

l = [0, 1, 2, 4]
for i in range(4, 11):
    l.append((l[i - 1] + l[i - 2] + l[i - 3]))

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    print(l[N])