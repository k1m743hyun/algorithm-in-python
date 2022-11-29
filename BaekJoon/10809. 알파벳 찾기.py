word = input()

alpha = {chr(97 + i): -1 for i in range(26)}
for i, v in enumerate(word):
    if alpha[v] == -1:
        alpha[v] = i

print(' '.join(map(str, alpha.values())))
