import sys

stack = []

n = int(sys.stdin.readline())
for _ in range(n):
    line = sys.stdin.readline().split()
    if line[0] == 'push':
        stack.append(int(line[1]))
    elif line[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif line[0] == 'size':
        print(len(stack))
    elif line[0] == 'empty':
        print(0 if stack else 1)
    elif line[0] == 'top':
        print(stack[-1] if stack else -1)