n = int(input())

num = 1
step = 6
cnt = 1
while True:
    if num >= n:
        break
    num += step
    step += 6
    cnt += 1

print(cnt)
