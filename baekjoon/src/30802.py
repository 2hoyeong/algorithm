N = int(input())
S = map(int, input().split())
T, P = map(int, input().split())

TP = 0
for s in S:
    TP += (s // T) + 1
    if s % T == 0:
        TP -= 1

print(TP)
print(f"{N // P} {N % P}")
