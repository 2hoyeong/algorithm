# 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

answer = A * B * C

counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for word in str(answer):
    counter[int(word)] += 1

for i in counter:
    print(i)