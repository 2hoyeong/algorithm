N = int(input())
M = int(input())
S = input()

cursor = 0
answer = 0
count = 0

while cursor < M - 1:
    if S[cursor:cursor + 3] == "IOI":
        count += 1
        cursor += 2

        if count == N:
            answer += 1
            count -= 1
    else:
        count = 0
        cursor += 1

print(answer)
