# Enter your code here. Read input from STDIN. Print output to STDOUT

word_dict = {}
for word in [input() for _ in range(int(input()))]:
    if word not in word_dict:
        word_dict[word] =  1
    else:
        word_dict[word] += 1

print(len(word_dict))
for k, v in word_dict.items():
    print(v, end=' ')