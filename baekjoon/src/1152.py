#단어의 개수

import sys

count = 0
for _ in map(str, sys.stdin.readline().rstrip().split()):
    count += 1

print(count)
