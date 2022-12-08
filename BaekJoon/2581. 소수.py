import math

m = int(input())
n = int(input())

sum_val = 0
min_val = n
for num in range(m, n + 1):
    if num == 1:
        continue

    flag = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            flag = 1
            break

    if not flag:
        sum_val += num
        if num < min_val:
            min_val = num

print(sum_val if sum_val else -1)
if sum_val:
    print(min_val)
