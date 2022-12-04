n = int(input())

cnt = 0
for _ in range(n):
    word = input()
    char_dict = {char: word.index(char) for char in word}

    flag = 1
    for i, v in enumerate(word):
        if i != char_dict[v]:
            if i == char_dict[v] + 1:
                char_dict[v] = i
            else:
                flag = 0
                break

    if flag:
        cnt += 1

print(cnt)
