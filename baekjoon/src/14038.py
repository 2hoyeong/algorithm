w = 0
for _ in range(6):
    g = input()
    if g == "W":
        w += 1

if w >= 5:
    print("1")
elif w >= 3:
    print("2")
elif w >= 1:
    print("3")
else:
    print("-1")
