a, b = map(int, input().split())
c = int(input())

m = b + c
print((a + m // 60) % 24, m % 60)
