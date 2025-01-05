K, N = map(int, input().split())

cables = []
for _ in range(K):
    cables.append(int(input()))

left, right = 1, max(cables)

while left <= right:
    mid = (left + right) // 2
    counts = [c // mid for c in cables]
    if sum(counts) >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)
