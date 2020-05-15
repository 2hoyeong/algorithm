# https://www.acmicpc.net/problem/2751
# 수 정렬하기 2

N = int(input())
q = []
for _ in range(N):
    q.append(int(input()))

q.sort()
for e in q:
    print(e)