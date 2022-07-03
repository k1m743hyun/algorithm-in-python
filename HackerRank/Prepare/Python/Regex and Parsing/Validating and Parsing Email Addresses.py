# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

email_addr = re.compile('^\<[A-Za-z](\w|-|\.|_)+\@[A-Za-z]+\.[A-Za-z]{1,3}\>$')

n = int(input())
for _ in range(n):
    name, addr = input().split()
    
    if email_addr.match(addr):
        print(' '.join([name, addr]))
