# 너의 핸들은
N, I = map(int, input().split())
handle = []
for _ in range(N):
    handle.append(input())
handle.sort()
print(handle[I - 1])