# A+B - 6
import sys

T = sys.stdin.readline()
for _ in range(int(T)):
    op1,op2 = input().split(',')
    result = eval(op1) + eval(op2)
    print(result)