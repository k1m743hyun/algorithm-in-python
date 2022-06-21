# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

s, n = input().split()

result = []
for i in range(1, int(n)+1):
    result += [''.join(c) for c in combinations(sorted(list(s)), i)]

for w in result:
    print(w)
