fibonacci = []
counter = []
for x in range(41):
    fibonacci.append(0)
    counter.append([0, 0])
    if x == 0:
        counter[x][0] += 1
        fibonacci[0] = 0
    elif x == 1:
        counter[x][1] += 1
        fibonacci[1] = 1
    else:
        fibonacci[x] = fibonacci[x-1] + fibonacci[x-2]
        counter[x][0] = counter[x-1][0] + counter[x-2][0]
        counter[x][1] = counter[x-1][1] + counter[x-2][1]

for _ in range(int(input())):
    N = int(input())
    print(counter[N][0], counter[N][1])