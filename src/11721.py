# 열 개씩 끊어 출력하기
X = input()

result = ""
for i in range(1, len(X) + 1):
    result += X[i - 1]

    if i % 10 == 0:
        print(result)
        result = ""
print(result)