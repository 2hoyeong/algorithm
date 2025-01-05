N = int(input())

rooms = 1
while N > 1:
    N -= 6 * rooms
    rooms += 1

print(rooms)
