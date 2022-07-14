import numpy as np

p = list(map(float, input().split()))
x = int(input())

print(np.polyval(p, x))
