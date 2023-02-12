class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n * 1 if n % 2 == 0 else n * 2


if __name__ == '__main__':
    # Test Case 1
    n = 5
    print(Solution().smallestEvenMultiple(n))  # 10

    # Test Case 2
    n = 6
    print(Solution().smallestEvenMultiple(n))  # 6
