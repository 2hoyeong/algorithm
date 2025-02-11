import sys
import heapq


h = []
for _ in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())

    if x == 0:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, x)
