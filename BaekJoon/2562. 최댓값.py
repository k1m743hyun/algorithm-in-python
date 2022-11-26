num_list = [int(input()) for _ in range(9)]

max_idx = 0
max_num = 0
for i, v in enumerate(num_list):
    if v > max_num:
        max_idx = i
        max_num = v

print(max_num)
print(max_idx + 1)
