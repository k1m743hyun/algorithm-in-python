# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

dow = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

m, d, y = map(int, input().split())
print(dow[calendar.weekday(y, m, d)])
