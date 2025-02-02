import sys
N, M = map(int, input().split())

sites = {}
for _ in range(N):
    site, password = sys.stdin.readline().rstrip().split()
    sites[site] = password

for _ in range(M):
    site = sys.stdin.readline().rstrip()
    print(sites[site])
