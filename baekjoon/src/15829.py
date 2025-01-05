L = int(input())

s = input()
result = 0

for i in range(L):
    c = ord(s[i]) - ord('a') + 1
    result += c * (31 ** i)

print(result % 1234567891)
