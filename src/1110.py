# 더하기 사이클

X = input()
if len(X) != 2:
    X = "0" + X

_X = int(X)

count = 0
tmp = X
origin = _X
while True:
    count += 1
    tmp = str(tmp[1] + str((int(tmp[0]) + int(tmp[1]))%10))
    if int(tmp) is origin: break

print(count)