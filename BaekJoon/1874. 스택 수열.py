import sys

n = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
result = []

idx = 0
for num in range(1, n + 1):
    result.append('+')
    stack.append(num)

    while idx < n and stack[-1] == num_list[idx]:
        result.append('-')
        stack.pop()
        idx += 1
        if not stack:
            break

if stack:
    print('NO')
else:
    for r in result:
        print(r)