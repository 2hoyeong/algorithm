import sys

N = int(sys.stdin.readline())

prime_number = [True] * (N + 1)
prime_number[0] = False
prime_number[1] = False

for i in range(2, N // 2 + 1):
	if prime_number[i] == True:
		for j in range(i + i, N + 1, i):
			prime_number[j] = False
		
prime_number = [x for x in range(len(prime_number)) if prime_number[x]]

l, r = 0, 0
answer = 0
n = len(prime_number)
while l <= n and r <= n:
        prime_sum = sum(prime_number[l:r])
        if prime_sum < N:
                r += 1
        elif prime_sum > N:
                l += 1
        else:
                l += 1
                answer += 1

print(answer)
