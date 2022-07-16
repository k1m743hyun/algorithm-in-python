import numpy as np

n, m = map(int, input().split())

a = np.array([list(map(int, input().split())) for _ in range(n)])

print(np.max(np.min(a, axis=1)))
