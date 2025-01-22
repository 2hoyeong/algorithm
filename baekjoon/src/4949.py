while True:
    s = input()
    if s == ".":
        break
    
    stack = []
    passed = True
    for c in s:
        if c == "(" or c == "[":
            stack.append(c)
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                passed = False
                break
        elif c == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                passed = False
                break

    if stack or not passed:
        print('no')
    else:
        print('yes')
