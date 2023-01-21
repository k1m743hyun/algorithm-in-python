import math


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, list(str(n))))
        return math.prod(digits) - sum(digits)


if __name__ == '__main__':
    # Test Case 1
    n = 234
    print(Solution().subtractProductAndSum(n))  # 15

    # Test Case 2
    n = 4421
    print(Solution().subtractProductAndSum(n))  # 21
