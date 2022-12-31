import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
q = deque([i + 1 for i in range(n)])

result = []
while True:
    q.rotate(-1 * (k - 1))
    result.append(q.popleft())
    if len(q) < 1:
        break

print('<' + ', '.join(map(str, result)) + '>')
