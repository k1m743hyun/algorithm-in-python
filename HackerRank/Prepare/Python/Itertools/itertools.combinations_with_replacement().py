# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

s, n = input().split()
for k in sorted([''.join(sorted(j)) for j in [i for i in combinations_with_replacement(s, int(n))]]):
    print(k)
