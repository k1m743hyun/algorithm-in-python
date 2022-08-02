# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    line = ''.join(sorted(input()))
    
    flag = 0
    
    # It must contain at least 2 uppercase English alphabet characters.
    if not re.search(r'[A-Z]{2}', line):
        flag = 1
    
    # It must contain at least 3 digits (0 - 9).
    if not re.search(r'\d\d\d', line):
        flag = 1
    
    # It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
    if re.search(r'[^a-zA-Z0-9]', line):
        flag = 1
    
    # No character should repeat.
    if re.search(r'(.)\1', line):
        flag = 1
    
    # There must be exactly  characters in a valid UID.
    if len(line) != 10:
        flag = 1

    print('Invalid' if flag else 'Valid')
