import sys

N, M = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

l, r = 0, 1
answer = 0
min_len = N
seq_sum = sum(seq)
if seq_sum < M:
        print(0)
elif seq_sum == M:
        print(N)
else:
        seq_sum = seq[0]
        while l < N:
                if seq_sum >= M:
                        min_len = min(min_len, r - l)
                        seq_sum -= seq[l]
                        l += 1
                else:
                        if r == N:
                                l += 1
                        else:
                                seq_sum += seq[r]
                                r += 1
                        

        print(min_len)
