import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
for p in permutations([i+1 for i in range(n)], m):
    print(' '.join(map(str, p)))
