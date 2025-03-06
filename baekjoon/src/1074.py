N, r, c = map(int, input().split())
count = 0
done = False
def divide(x, y, n):
    global count, done
    if done:
        return
    if n == 2:
        if x == r and y == c:
            done = True
            return
        if x == r and y + 1 == c:
            count += 1
            done = True
            return
        if x + 1 == r and y == c:
            count += 2
            done = True
            return
        if x + 1 == r and y + 1 == c:
            count += 3
            done = True
            return
        count += 4
    else:
        if x + n // 2 > r and y + n // 2 > c:
            divide(x, y, n // 2)
        else:
            if not done:
                count += (n // 2) ** 2

        if x + n // 2 > r and y + n // 2 <= c:
            divide(x, y + n // 2, n // 2)
        else:
            if not done:
                count += (n // 2) ** 2
        
        if x + n // 2 <= r and y + n // 2 > c:
            divide(x + n // 2, y, n // 2)
        else:
            if not done:
                count += (n // 2) ** 2
        
        if x + n // 2 <= r and y + n // 2 <= c:
            divide(x + n // 2, y + n // 2, n // 2)
        else:
            if not done:
                count += (n // 2) ** 2

divide(0, 0, 2 ** N)
print(count)
