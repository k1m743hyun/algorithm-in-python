import math

n = int(input())
num_list = list(map(int, input().split()))

cnt = 0
for num in num_list:
    if num == 1:
        continue

    flag = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            flag = 1
            break

    if not flag:
        cnt += 1

print(cnt)
