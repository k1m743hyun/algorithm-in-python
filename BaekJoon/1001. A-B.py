print(sum([v if i % 2 == 0 else -v for i, v in enumerate(map(int, input().split()))]))
