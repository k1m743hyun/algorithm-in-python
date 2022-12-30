import sys
from collections import deque

q = deque([])

n = int(sys.stdin.readline())
for _ in range(n):
    line = sys.stdin.readline().split()
    if line[0] == 'push':
        q.append(int(line[1]))
    elif line[0] == 'pop':
        print(q.popleft() if q else -1)
    elif line[0] == 'size':
        print(len(q))
    elif line[0] == 'empty':
        print(0 if q else 1)
    elif line[0] == 'front':
        print(q[0] if q else -1)
    elif line[0] == 'back':
        print(q[-1] if q else -1)