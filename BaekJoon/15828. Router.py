import sys
from collections import deque

buffer_size = int(sys.stdin.readline())
buffer = deque([])

while True:
    packet = int(sys.stdin.readline())

    if packet == -1:
        break
    elif packet == 0:
        buffer.popleft()
    else:
        if len(buffer) < buffer_size:
            buffer.append(packet)

print(' '.join(map(str, buffer)) if buffer else 'empty')