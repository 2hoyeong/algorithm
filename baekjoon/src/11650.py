N = int(input())

coords = []
for _ in range(N):
    x, y = map(int, input().split())
    coords.append([x, y])

coords.sort(key=lambda x:(x[0], x[1]))

for coord in coords:
    print(coord[0], coord[1])
