# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
num_list = list(map(int, input().split()))

print(all(list(map(lambda x: x > 0, num_list))) and any(list(map(lambda x: str(x)[0] == str(x)[-1], num_list))))
