# 2007년

import sys

wDay = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
mDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
a, b = map(int, sys.stdin.readline().rstrip().split())
days = 0
a = a - 1
for i in range(a):
    days += mDays[i]
days += b
days = days % 7
print(wDay[days])