# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

for c in b:
    if c in a:
        print(' '.join([str(i + 1) for i, e in enumerate(a) if e == c]))
    else:
        print(-1)
