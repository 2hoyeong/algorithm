N = int(input())

people = []
for _ in range(N):
    weight, height = map(int, input().split())
    people.append([weight, height, 0])

for person in people:
    rank = 1
    for weight, height, _ in people:
        if person[0] < weight and person[1] < height:
            rank += 1
    person[2] = rank

for person in people:
  print(person[2], end=' ')
