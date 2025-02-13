import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = sys.stdin.readline().rstrip()
    array_strings = sys.stdin.readline().rstrip()
    if n == "0":
        arr = deque()
    else:
        arr = deque(array_strings[1:-1].split(","))
        
    
    error = False
    reverse_toggle = False
    for op in p:
        if op == "R":
            reverse_toggle = not reverse_toggle
        elif op == "D":
            if len(arr) == 0:
                error = True
                break
            else:
                if reverse_toggle:
                    arr.pop()
                else:
                    arr.popleft()
    
    if error == True:
        print("error")
    else:
        if reverse_toggle:
            arr.reverse()
        print(f"[{','.join(arr)}]")
