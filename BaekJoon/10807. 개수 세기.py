n = int(input())
num_list = list(map(int, input().split()))
v = int(input())

cnt = 0
for num in num_list:
    if num == v:
       cnt += 1

print(cnt)
