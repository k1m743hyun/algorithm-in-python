import sys
from collections import deque

deq = deque([])

n = int(sys.stdin.readline())
for _ in range(n):
    line = sys.stdin.readline().split()
    if line[0] == 'push_front':
        deq.appendleft(int(line[1]))
    elif line[0] == 'push_back':
        deq.append(int(line[1]))
    elif line[0] == 'pop_front':
        print(deq.popleft() if deq else -1)
    elif line[0] == 'pop_back':
        print(deq.pop() if deq else -1)
    elif line[0] == 'size':
        print(len(deq))
    elif line[0] == 'empty':
        print(0 if deq else 1)
    elif line[0] == 'front':
        print(deq[0] if deq else -1)
    elif line[0] == 'back':
        print(deq[-1] if deq else -1)
