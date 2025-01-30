import sys

M = int(sys.stdin.readline())

s = 0

for _ in range(M):
    ops = sys.stdin.readline().rstrip().split()
    if ops[0] == "empty":
        s = 0
    elif ops[0] == "add":
        s |= (1 << int(ops[1]))
    elif ops[0] == "remove":
        s &= ~(1 << int(ops[1]))
    elif ops[0] == "check":
        print(1 if s & (1 << int(ops[1])) != 0 else 0)
    elif ops[0] == "toggle":
        s ^= (1 << int(ops[1]))
    elif ops[0] == "all":
        s ^= (1 << 21) - 1
