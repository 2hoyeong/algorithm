s = input()

minuses = s.split("-")

for i in range(len(minuses)):
    minuses[i] = sum(map(int, minuses[i].split("+")))

result = minuses[0]
for minus in minuses[1:]:
    result -= minus

print(result)
