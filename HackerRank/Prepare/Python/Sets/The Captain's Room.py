# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

k = int(input())
room = list(map(int, input().split()))

for k, v in Counter(room).items():
    if v == 1:
        print(k)
        break