# 계단 오르기
import sys

stair = int(sys.stdin.readline().rstrip())
point = [0]
for _ in range(stair):
    point.append(int(sys.stdin.readline().rstrip()))

maxp = [[0, 0], [point[1], point[1]], [0 + point[2], point[1] + point[2]]]
step = [0]
for i in range(3, stair + 1):
    maxp.append([
        max(maxp[i - 2][0], maxp[i - 2][1]) + point[i],
        maxp[i - 1][0] + point[i]
    ])

print(max(maxp[stair][0], maxp[stair][1]))