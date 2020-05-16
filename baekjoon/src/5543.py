# https://www.acmicpc.net/problem/5543
# 상근날드

burger = []
for _ in range(3):
    burger.append(int(input()))
cola = int(input())
cidar = int(input())

print(min(burger) + min(cola, cidar) - 50)
