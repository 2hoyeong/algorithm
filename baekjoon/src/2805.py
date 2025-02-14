N, M = map(int, input().split())
trees = list(map(int, input().split()))

left, right = 0, max(trees)
answer = 0
while left < right:
    mid = (right + left) // 2

    sliced = 0
    for tree in trees:
        sliced += max(0, tree - mid)

    if sliced > M:
        left = mid + 1
        answer = mid
    elif sliced < M:
        right = mid
    else:
        answer = mid
        break

print(answer)
