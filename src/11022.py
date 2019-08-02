# A+B - 8
import sys

T = sys.stdin.readline().rstrip()
for i in range(int(T)):
    op1, op2 = input().split()
    result = eval(op1) + eval(op2)
    print("Case #"+str(i + 1)+":", op1, "+", op2, "=", result)