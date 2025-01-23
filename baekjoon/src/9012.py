T = int(input())

for _ in range(T):
    s = input()
    stack = []

    passed = True
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack or stack[-1] != "(":
                passed = False
                break
            else:
                stack.pop()
    
    if not passed or stack:
        print('NO')
    else:
        print('YES')

