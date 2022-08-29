# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

phone_number = re.compile('^[7-9]{1}[0-9]{9}$')

n = int(input())
for _ in range(n):
    line = input()
    print('YES' if phone_number.match(line) else 'NO')
