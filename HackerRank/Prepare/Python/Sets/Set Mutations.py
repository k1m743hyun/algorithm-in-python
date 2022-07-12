# Enter your code here. Read input from STDIN. Print output to STDOUT
length = int(input())
a = set(map(int, input().split()))

n = int(input())
for _ in range(n):
    line = input().split()
    b = set(map(int, input().split()))
    
    if line[0] == 'update':
        a.update(b)
    elif line[0] == 'intersection_update':
        a.intersection_update(b)
    elif line[0] == 'difference_update': 
        a.difference_update(b)
    elif line[0] == 'symmetric_difference_update':
        a.symmetric_difference_update(b)
    else:
        pass

print(sum(a))
