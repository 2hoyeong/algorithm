# 알파벳 찾기
import sys

T = sys.stdin.readline().rstrip()

for a in range(97, 123):
    print(str(T.find(chr(a))) + " ", end='')