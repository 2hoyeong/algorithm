import math

N = int(input())

num = str(math.factorial(N))
cursor = len(num) - 1

while cursor > 0:
    if num[cursor] != '0':
        break
    cursor -= 1

print(len(num) - cursor - 1)
