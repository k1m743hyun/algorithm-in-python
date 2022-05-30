# Enter your code here. Read input from STDIN. Print output to STDOUT
x = int(input())
size_list = list(map(int, input().split()))

sell = 0
n = int(input())
for _ in range(n):
    size, price = map(int, input().split())
    
    if size in size_list:
        size_list.pop(size_list.index(size))
        sell += price

print(sell)