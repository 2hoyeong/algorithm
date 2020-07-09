import sys

N, M = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

l, r = 0, 0
answer = 0
while l <= N and r <= N:
	seq_sum = sum(seq[l:r])
	if seq_sum < M:
		r += 1
	elif seq_sum > M:
		l += 1
	else:
		l += 1
		answer += 1

print(answer)
