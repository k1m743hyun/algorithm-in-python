# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for _ in range(n):
    line = input()

    line = re.sub('(?<= )(\&\&)(?= )', 'and', line)
    line = re.sub('(?<= )(\|\|)(?= )', 'or', line)

    print(line)
