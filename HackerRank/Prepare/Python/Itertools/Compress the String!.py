# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()

cnt = 0
result = []
for idx, num in enumerate(s):
    cnt += 1
    if (idx == len(s) - 1) or (s[idx] != s[idx + 1]):
        result.append(str((cnt, int(num))))
        cnt = 0

print(' '.join(result))