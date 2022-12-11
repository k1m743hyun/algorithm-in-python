import sys

num_dict = {}
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num_dict.get(num):
        num_dict[num] += 1
    else:
        num_dict[num] = 1

for num, cnt in sorted(num_dict.items()):
    for _ in range(cnt):
        print(num)
