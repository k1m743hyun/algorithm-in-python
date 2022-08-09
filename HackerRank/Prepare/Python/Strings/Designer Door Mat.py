# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

i = 1
while i <= n - 2:
    print(('.|.' * i).center(m, '-'))
    i += 2

print('WELCOME'.center(m, '-'))

i = n - 2
while i >= 1:
    print(('.|.' * i).center(m, '-'))
    i -= 2
