N = int(input())
fruits = list(map(int, input().split()))

left, right = 0, 0
stick = { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
result = 0

def get_count():
    count = 0
    for i in range(1, 10):
        if stick[i] > 0:
            count += 1
    return count
        

while right < N:
    stick[fruits[right]] += 1

    while get_count() > 2:
        stick[fruits[left]] -= 1
        left += 1

    result = max(result, right - left + 1)
    right += 1

print(result)
