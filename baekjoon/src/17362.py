# 수학은 체육과목 입니다 2
a = int(input())

if a == 9:
    print("1")
elif a <= 5:
    print(a)
else:
    a = a % 8
    if a == 0:
        a = 8
    if a <= 5:
        print(a)
    else:
        print(10 - a)