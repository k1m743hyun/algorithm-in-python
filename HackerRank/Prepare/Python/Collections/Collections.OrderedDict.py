# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())

d = OrderedDict()
for _ in range(n):
    line = input().split()
    k, v = ' '.join(line[:-1]), int(line[-1])
    
    if d.get(k):
        d[k] += int(v)
    else:
        d[k] = v
        
for k, v in d.items():
    print(k, v)