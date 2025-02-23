import heapq
import sys
from collections import defaultdict

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    g_heap = []
    m_heap = []
    g_excludes = defaultdict(int)
    m_excludes = defaultdict(int)

    for _ in range(int(sys.stdin.readline().rstrip())):
        op, data = sys.stdin.readline().rstrip().split()
        data = int(data)
        if op == "I":
            heapq.heappush(g_heap, data)
            heapq.heappush(m_heap, data * -1)
        elif op == "D":
            if data == 1 and m_heap:
                maximum = heapq.heappop(m_heap) * -1
                g_excludes[maximum] = g_excludes.get(maximum, 0) - 1
            elif data == -1 and g_heap:
                minimum = heapq.heappop(g_heap)
                m_excludes[minimum] = m_excludes.get(minimum, 0) - 1

            while g_heap and g_excludes.get(g_heap[0], 0) < 0:
                g_excludes[g_heap[0]] += 1
                heapq.heappop(g_heap)
            while m_heap and m_excludes.get(m_heap[0] * -1, 0) < 0:
                m_excludes[m_heap[0] * -1] += 1
                heapq.heappop(m_heap)

    if len(m_heap) == 0 or len(g_heap) == 0:
        print("EMPTY")
    else:
        print(f"{m_heap[0] * -1} {g_heap[0]}")
