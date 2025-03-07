import sys

meetings = []

for _ in range(int(input())):
    start, end = map(int, sys.stdin.readline().rstrip().split())

    meetings.append([start, end])

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
end = 0
for meeting in meetings:
    if end <= meeting[0]:
        count += 1
        end = meeting[1]

print(count)
