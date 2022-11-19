total = int(input())
for _ in range(int(input())):
    price, each = map(int, input().split())
    total -= price * each

print('No' if total else 'Yes')
