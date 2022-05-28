# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()

result = {'lower': [], 'upper': [], 'odd': [], 'even': []}
for i in s:
    if i.isdigit():
        if int(i) % 2 == 0:
            result['even'].append(i)
        else:
            result['odd'].append(i)
    else:
        if i.isupper():
            result['upper'].append(i)
        else:
            result['lower'].append(i)

print(''.join(sorted(result['lower']) + sorted(result['upper']) + sorted(result['odd']) + sorted(result['even'])))