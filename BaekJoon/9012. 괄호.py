import sys

t = int(sys.stdin.readline())
for _ in range(t):
    stack = []

    flag = 1
    for char in sys.stdin.readline():
        if char == '(':
            stack.append('(')

        elif char == ')':
            if not stack or stack.pop() != '(':
                flag = 0
                break

    if stack:
        flag = 0

    print('YES' if flag else 'NO')