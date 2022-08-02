# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()
k = input()

m = list(re.finditer(r'(?={})'.format(k), s))
if m:
    for i in m:
        s, e = i.span()
        print('({}, {})'.format(s, s+len(k)-1))
else:
    print('(-1, -1)')
