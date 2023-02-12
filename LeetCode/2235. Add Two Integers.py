class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2


if __name__ == '__main__':
    # Test Case 1
    num1 = 12
    num2 = 5
    print(Solution().sum(num1, num2))  # 17

    # Test Case 2
    num1 = -10
    num2 = 4
    print(Solution().sum(num1, num2))  # -6
