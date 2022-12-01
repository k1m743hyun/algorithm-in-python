dial = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5: 'JKL', 6: 'MNO', 7: 'PQRS', 8: 'TUV', 9: 'WXYZ'}
alpha_num = {a: k for k, v in dial.items() for a in v}

total = 0
for alpha in input():
    total += alpha_num[alpha] + 1

print(total)
