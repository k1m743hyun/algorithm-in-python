n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    line = input().split()

    if line[0] == 'pop':
        s.pop()
    elif line[0] == 'remove':
        s.remove(int(line[1]))
    elif line[0] == 'discard':
        s.discard(int(line[1]))

print(sum(s))
