n = int(input())

for _ in range(n):
    result = input()

    score = 0
    temp = 1
    for i, v in enumerate(result):
        if v != 'X':
            if i != 0:
                if v == result[i - 1]:
                    temp += 1
                else:
                    temp = 1
            score += temp

    print(score)
