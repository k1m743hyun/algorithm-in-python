import sys

t = int(sys.stdin.readline())
for _ in range(t):
    stack = 0

    flag = 1
    for ps in sys.stdin.readline()[:-1]:
        if ps == '(':
            stack += 1
        else:
            if stack == 0:
                flag = 0
                break
            stack -= 1


    print('YES' if flag and stack == 0 else 'NO')