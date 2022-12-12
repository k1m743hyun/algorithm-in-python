n = int(input())
num_list = list(map(int, input().split()))

num_dict = {val: idx for idx, val in enumerate(sorted(set(num_list)))}
print(' '.join([str(num_dict[num]) for num in num_list]))
