# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for _ in range(n):
    line = input()
    
    if re.compile('^[4-6][0-9]{3}-*[0-9]{4}-*[0-9]{4}-*[0-9]{4}').match(line):
        flag = 1
        line_list = line.split('-')
        
        if '' in line_list:
            flag = 0
            
        else:
            new_line = ''.join(line_list)

            if len(new_line) != 16:
                flag = 0
                
            else:
                cnt = 1
                for i, l in enumerate(new_line):
                    if i == 0:
                        pass
                    
                    elif cnt > 3:
                        flag = 0
                        break
                    
                    elif l == new_line[i-1]:
                        cnt += 1
                        
                    else:
                        cnt = 1
    
    else:
        flag = 0
    
    if flag == 1:
        print('Valid')
    else:
        print('Invalid')