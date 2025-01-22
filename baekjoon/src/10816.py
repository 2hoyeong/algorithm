import sys

_ = sys.stdin.readline()

cards = sys.stdin.readline().split()

dict = {}

for card in cards:
    if card in dict:
        dict[card] += 1
    else:
        dict[card] = 1

_ = sys.stdin.readline()

counting = sys.stdin.readline().split()
answer = []

for c in counting:
    if c in dict:
        answer.append(str(dict[c]))
    else:
        answer.append("0")

print(" ".join(answer))
