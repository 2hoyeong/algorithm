N, K = map(int, input().split())

table = [x for x in range(1, N + 1)]
target = [-1] * N
cursor = (K % N) - 1
answer = []

while True:
    answer.append(str(table[cursor]))
    table[cursor] = -1

    if table == target:
        break
    
    move = 0
    while move != K:
        cursor = (cursor + 1) % N
        if table[cursor] != -1:
            move += 1

print("<", ", ".join(answer), ">", sep="")
