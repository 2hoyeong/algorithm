import sys

N = int(input())

S = list()
R = ""
for _ in range(N):
    S.append(sys.stdin.readline().rstrip())

for i in range(len(S[0])):
    C = S[0][i]
    BOOL = True
    for j in range(1, N):
        if S[j][i] != C:
            R += "?"
            BOOL = False
            break
    if BOOL:
        R += C
print(R)