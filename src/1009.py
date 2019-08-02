import sys

T = int(sys.stdin.readline())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    a = a % 10
    b = b % 4
    if b == 0:
        b = 4
    dc = a ** b
    dc = dc % 10
    if dc == 0:
	    print("10")
    else:
        print(dc)