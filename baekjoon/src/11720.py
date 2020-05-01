# 숫자의 합
N = int(input())
X = input()

result = 0
for i in range(N):
    result += int(X[i])

print(result)