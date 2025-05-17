N = int(input())

memo = { 0: 0, 1: 1, 2: 1 }
if N <= 2:
    print(memo[N])
else:
    stack = [N]
    while stack:
        n = stack.pop()
        if n in memo:
            continue
        
        if n % 2 == 0:
            if n + 1 in memo and n - 1 in memo:
                memo[n] = (memo[n + 1] - memo[n - 1]) % 1000000007
            else:
                stack.append(n)
                stack.append(n + 1)
                stack.append(n - 1)
        else:
            if n // 2 in memo and n // 2 + 1 in memo:
                memo[n] = (memo[n // 2] ** 2 + memo[n // 2 + 1] ** 2) % 1000000007
            else:
                stack.append(n)
                stack.append(n // 2)
                stack.append(n // 2 + 1)

    print(memo[N])