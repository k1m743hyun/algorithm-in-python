# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for _ in range(t):
    n = int(input())
    blocks = list(map(int, input().split()))

    i = 0
    while i < len(blocks) - 1 and blocks[i] >= blocks[i + 1]:
        i += 1
    while i < len(blocks) - 1 and blocks[i] <= blocks[i + 1]:
        i += 1

    print('Yes' if i == len(blocks) - 1 else 'No')
