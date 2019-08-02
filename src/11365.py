# !밀비 급일
import sys

while True:
    S = sys.stdin.readline().rstrip()
    if S == "END":
        break
    for i in range(len(S)):
        print(S[len(S) - i - 1], end='')
    print()