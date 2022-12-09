import math

n = int(input())
while True:
    if n == 1:
        break

    flag = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            flag = 1
            n //= i
            print(i)
            break

    if not flag:
        print(n)
        break
