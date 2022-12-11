import sys
from collections import Counter

# 숫자 입력
num_list = sorted([int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))])
num_len = len(num_list)

# 산술평균
print(round(sum(num_list) / num_len))

# 중앙값
print(num_list[num_len // 2])

# 최빈값
num_most = Counter(num_list).most_common(2)
print(num_most[0][0] if len(num_most) == 1 else num_most[0][0] if num_most[0][1] != num_most[1][1] else num_most[1][0])

# 범위
print(num_list[-1] - num_list[0])
