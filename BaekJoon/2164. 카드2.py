import sys
from collections import deque

q = deque([i + 1 for i in range(int(sys.stdin.readline()))])

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])
