import sys

n, m = map(int, sys.stdin.readline().split())

sum_list = [0]
sum = 0
for i in map(int, sys.stdin.readline().split()):
    sum += i
    sum_list.append(sum)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_list[j] - sum_list[i-1])
