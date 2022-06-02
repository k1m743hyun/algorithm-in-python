import re

if __name__ == '__main__':
    s = input()
    
    for pattern in ['[A-Za-z0-9]+', '[A-Za-z]+', '[0-9]+', '[a-z]+', '[A-Z]+']:
        print(True if re.compile(pattern).findall(s) else False)
