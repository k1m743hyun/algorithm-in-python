import numpy as np

n, m = map(int, input().split())

print(np.prod(np.array(list(map(sum, zip(*[list(map(int, input().split())) for _ in range(n)]))))))
