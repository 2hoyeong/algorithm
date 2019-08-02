# 1로 만들기

X = int(input())
l = []
l.append(0)
l.append(0)
l.append(1)
l.append(1)

for i in range(4, X + 1):
    o = l[i - 1] + 1

    if i % 2 == 0:
        d2 = l[int(i / 2)] + 1
    else:
        d2 = 99999999
    if i % 3 == 0:
        d3 = l[int(i / 3)] + 1
    else:
        d3 = 99999999

    least = min(min(d2, d3), o)

    l.append(least)
print(l[X])