# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

color_pattern = '#[A-Fa-f0-9]{3,6}'

code_comp = re.compile('[ :]+' + color_pattern)
color_comp = re.compile(color_pattern)

result = []
for _ in range(n):
    line = input()
    result += code_comp.findall(line)

for i in map(color_comp.findall, result):
    print(i[0])
