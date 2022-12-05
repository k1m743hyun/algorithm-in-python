plastic_bag = [5, 3]

n = int(input())

cnt = 0
for size in plastic_bag:
    cnt += n // size
    n = n % size

    if size == 5:
        if cnt > 0 and (n == 1 or n == 4):
            cnt -= 1
            n += 5
        elif cnt > 1 and n == 2:
            cnt -= 2
            n += 10

print(-1 if n else cnt)
