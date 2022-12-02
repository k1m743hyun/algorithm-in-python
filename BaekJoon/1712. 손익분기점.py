a, b, c = map(int, input().split())
try:
    sell = (a // (c - b)) + 1
    print(-1 if sell < 0 else sell)
except Exception as e:
    print(-1)
