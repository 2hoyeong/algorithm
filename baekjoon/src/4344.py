# 평균은 넘겠지
import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    I = map(int, sys.stdin.readline().rstrip().split())
    L = list()
    C = 0
    N = next(iter(I))

    for i in I:
        L.append(i)
    A = sum(L) / len(L)

    for l in L:
        if l > A:
            C += 1

    print("{0:.3f}%".format(C / N * 100))