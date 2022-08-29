# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())
li = input().split()
cnt = int(input())

comb_list = list(combinations(li, cnt))
total = len(comb_list)

a = 0
for i in comb_list:
    if 'a' in i:
        a += 1

print(a / total)
