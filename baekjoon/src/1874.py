N = int(input())

stack = []
result = []
count = 1
NO = False

for _ in range(N):
    target = int(input())
    while count <= target:
        stack.append(count)
        result.append('+')
        count += 1

    if stack[-1] == target:
        result.append('-')
        stack.pop()
    else:
        NO = True
        break
if NO:
    print('NO')
else:
    print('\n'.join(result))
