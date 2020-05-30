# https://www.acmicpc.net/problem/1920
# 수 찾기

import sys

N = int(sys.stdin.readline())
numbers = set(map(int,sys.stdin.readline().split()))
_ = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))
for n in M:
    if(n in numbers):
        print("1")
    else:
        print("0")