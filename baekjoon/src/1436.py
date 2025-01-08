N = int(input())

n = 0
count = 0

while True:
    n += 1
    if '666' in str(n):
        count += 1

    if count == N:
        print(n)
        break
