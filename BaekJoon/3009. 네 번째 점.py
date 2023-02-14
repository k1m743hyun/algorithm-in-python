import sys

coords = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

answer = []
for coord in list(zip(*coords)):
    for c in set(coord):
        if coord.count(c) == 1:
            answer.append(c)

print(' '.join(map(str, answer)))