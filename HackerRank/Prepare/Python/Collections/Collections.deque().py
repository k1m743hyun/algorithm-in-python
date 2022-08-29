# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n = int(input())

dq = deque()
for _ in range(n):
    line = input().split()

    if 'append' in line[0]:
        if 'left' in line[0]:
            dq.appendleft(line[-1])
        else:
            dq.append(line[-1])
    else:
        if 'left' in line[0]:
            dq.popleft()
        else:
            dq.pop()

print(' '.join(dq))
