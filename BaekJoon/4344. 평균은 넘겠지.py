c = int(input())

for _ in range(c):
    temp = list(map(int, input().split()))

    n = temp[0]
    score = temp[1:]

    avg = sum(score) / n

    print('{:.3f}%'.format(sum([1 for s in score if s > avg]) / n * 100))
