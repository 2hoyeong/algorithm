T = int(input())

for _ in range(T):
    n = int(input())
    closet = {}
    for _ in range(n):
        _, type = input().split()
        if type in closet:
            closet[type] += 1
        else:
            closet[type] = 1
    answer = 1
    for v in closet.values():
        answer *= v + 1
    print(answer - 1)
