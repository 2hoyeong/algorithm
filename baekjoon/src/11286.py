import heapq
import sys

N = int(sys.stdin.readline().rstrip())

heap = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if heap:
            num = heapq.heappop(heap)
            print(num[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))
