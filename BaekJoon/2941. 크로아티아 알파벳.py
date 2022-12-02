word = input()
for c in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    word = word.replace(c, 'a')
print(len(word))
