import numpy as np

np.set_printoptions(legacy='1.13')

shape = tuple(map(int, input().split()))

print(np.zeros(shape, dtype=np.int))
print(np.ones(shape, dtype=np.int))