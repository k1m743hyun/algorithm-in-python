# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
n_list = list(map(int, input().split()))
a_list = set(map(int, input().split()))
b_list = set(map(int, input().split()))

score = 0
for i in n_list:
    if i in a_list:
        score += 1
    elif i in b_list:
        score -= 1

print(score)
