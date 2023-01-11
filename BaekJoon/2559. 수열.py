import sys

n, k = map(int, sys.stdin.readline().split())
temp_list = list(map(int, sys.stdin.readline().split()))

sum_list = [0]
sum = 0
for i in temp_list:
    sum += i
    sum_list.append(sum)

for i in range(len(sum_list) - k):
    v = sum_list[k + i] - sum_list[i]
    if i == 0:
        max_val = v
    elif v > max_val:
        max_val = v

print(max_val)
