N = int(input())

cons = 0
for i in range(1, N):
    M = str(i)
    if i + sum(map(int, M)) == N:
        cons = i
        break

print(cons)
