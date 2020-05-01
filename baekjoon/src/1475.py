# 방 번호

R = input()
NS = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for r in R:
    r = int(r)
    if r == 9:
        NS[6] += 1
    else:
        NS[r] += 1

NS[6] = int(NS[6] / 2 + 0.5)
print(max(NS))