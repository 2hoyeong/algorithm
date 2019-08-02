# X보다 작은 수
import sys

N, X = map(int, sys.stdin.readline().rstrip().split())

array = [None] * N
index = 0
for i in map(int, sys.stdin.readline().rstrip().split()):
    array[index] = i
    index += 1

output = ""
for pop in array:
    if pop < X:
        output += str(pop) + " "

output = output[0:-1]
print(output)