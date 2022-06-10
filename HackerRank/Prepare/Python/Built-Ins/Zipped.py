# Enter your code here. Read input from STDIN. Print output to STDOUT
column, row = map(int, input().split())

for v in list(map(lambda x: sum(x) / row, list(zip(*[list(map(float, input().split())) for _ in range(row)])))):
    print(v)