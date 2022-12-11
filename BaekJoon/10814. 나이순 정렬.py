for age, name in sorted([input().split() for _ in range(int(input()))], key=lambda x: int(x[0])):
    print(age, name)
