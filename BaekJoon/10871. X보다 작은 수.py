n, x = map(int, input().split())
num_list = map(int, input().split())

print(' '.join([str(num) for num in num_list if num < x]))
