N = int(input())

people = []
for _ in range(N):
    age, name = input().split()
    people.append([int(age), name])

people.sort(key=lambda x:x[0])

for person in people:
    print(person[0], person[1])
