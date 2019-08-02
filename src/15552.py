# 빠른 A+B
import sys

T = sys.stdin.readline()
for _ in range(int(T)):
    op1,op2 = map(int, sys.stdin.readline().rstrip().split())
    print(op1 + op2)