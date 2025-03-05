N = int(input())

answer = 0
for i in range(1, N): # 남규
    for j in range(1, N): # 영훈
        for k in range(1, N): # 택희
            if N - (i + j + k) == 0 and i - j >= 2 and k % 2 == 0:
                answer += 1

print(answer)
