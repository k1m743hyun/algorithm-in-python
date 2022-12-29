while True:
    line = input()

    if line == '.':
        break

    stack = []

    flag = 1
    for char in line:
        if char == '(':
            stack.append('(')

        elif char == ')':
            if not stack or stack.pop() != '(':
                flag = 0
                break

        elif char == '[':
            stack.append('[')

        elif char == ']':
            if not stack or stack.pop() != '[':
                flag = 0
                break

    if stack:
        flag = 0

    print('yes' if flag else 'no')