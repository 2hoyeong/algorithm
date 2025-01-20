import sys

def roundoff(target):
    integer = int(target)
    if (target - integer) >= 0.5:
        return integer + 1
    else:
        return integer

N = int(sys.stdin.readline())

if N == 0:
    print(0)
else: 
    level = 0
    levels = []
    exclude = roundoff(N * 0.15)

    for _ in range(N):
        levels.append(int(sys.stdin.readline()))

    levels.sort()

    levels = levels[exclude:N-exclude]

    print(roundoff(sum(levels) / (N - 2 * exclude)))
