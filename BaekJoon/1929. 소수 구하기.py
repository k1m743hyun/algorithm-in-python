import math

m, n = map(int, input().split())

for num in range(m, n + 1):
    if num == 1:
        continue

    flag = 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            flag = 1
            break

    if not flag:
        print(num)
