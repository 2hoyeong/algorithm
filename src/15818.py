# 오버플로우와 모듈러
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
ai = [int(i) for i in sys.stdin.readline().rstrip().split()]

result = 1
for i in range(N):
    result = ((ai[i] % M) * (result % M) % M)

print(result)