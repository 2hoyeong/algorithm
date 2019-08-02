# A+B - 4
import sys

while True:
    try:
        I = sys.stdin.readline().rstrip()
    except EOFError:
        break
    if not I:
        break
    A, B = map(int, I.split())

    print(A + B)