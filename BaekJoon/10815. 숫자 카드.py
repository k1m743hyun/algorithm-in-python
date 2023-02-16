import sys

n = int(sys.stdin.readline())
n_list = sys.stdin.readline().split()

m = int(sys.stdin.readline())
m_list = sys.stdin.readline().split()

print(' '.join(['1' if m in n_list else '0' for m in m_list]))
