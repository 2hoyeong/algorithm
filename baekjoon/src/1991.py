N = int(input())

graph = {}

for i in range(N):
    graph[chr(i + ord('A'))] = ['.', '.']
    
for _ in range(N):
    P, L, R = input().split()
    if L != '.':
        graph[P][0] = L
    if R != '.':
        graph[P][1] = R

def findPre(node):
    if node == '.':
        return ''

    return node + findPre(graph[node][0]) + findPre(graph[node][1])

def findMid(node):
    if node == '.':
        return ''

    return findMid(graph[node][0]) + node + findMid(graph[node][1])

def findPost(node):
    if node == '.':
        return ''

    return findPost(graph[node][0]) + findPost(graph[node][1]) + node

print(findPre('A'))
print(findMid('A'))
print(findPost('A'))
