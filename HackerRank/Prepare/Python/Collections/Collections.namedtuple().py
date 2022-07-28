# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

row_cnt = int(input())
Student = namedtuple('Student', ','.join(input().split()))

sum = 0
for idx in range(row_cnt):
    sum += int(Student(*input().split()).MARKS)

print(sum / row_cnt)