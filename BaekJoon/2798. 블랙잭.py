import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

for num in sorted(list(map(sum, combinations(cards, 3))), reverse=True):
    if num <= m:
        break

print(num)
