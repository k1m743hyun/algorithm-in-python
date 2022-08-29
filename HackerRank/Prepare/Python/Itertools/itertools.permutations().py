# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

s, n = input().split()

for word in sorted([''.join(i) for i in permutations(list(s.upper()), int(n))]):
    print(word)
