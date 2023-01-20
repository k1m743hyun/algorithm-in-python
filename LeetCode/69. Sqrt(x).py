class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)


if __name__ == '__main__':
    # Test Case 1
    x = 4
    print(Solution().mySqrt(x))  # 2

    # Test Case 2
    x = 8
    print(Solution().mySqrt(x))  # 2
