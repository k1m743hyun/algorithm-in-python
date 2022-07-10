import numpy as np

n, m = map(int, input().split())

result = np.array([list(map(int, input().split())) for _ in range(n)])
print(np.transpose(result))
print(result.flatten())
