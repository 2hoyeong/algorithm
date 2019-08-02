# A+B - 5

import sys

while True:
    op1, op2 = map(int, sys.stdin.readline().rstrip().split())
    if op1 == 0 and op2 == 0:
        break
    print(op1 + op2)