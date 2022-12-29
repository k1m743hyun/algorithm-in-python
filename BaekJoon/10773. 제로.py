import sys

stack = []

k = int(sys.stdin.readline())
for _ in range(k):
    num = int(sys.stdin.readline())
    if num:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))