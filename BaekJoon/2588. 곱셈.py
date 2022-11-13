a = int(input())
b = list(map(int, list(input())))
b.reverse()

result = 0
for i, v in enumerate(b):
    temp = a * v
    print(temp)
    result += temp * (10 ** i)

print(result)
