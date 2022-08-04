# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

t = int(input())
for _ in range(t):
    line = input()
    print(bool(re.match(r'[+-]?[0-9]*\.[0-9]+$', line)))
