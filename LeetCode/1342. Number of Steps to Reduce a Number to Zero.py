class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
                step += 1
            else:
                num -= 1
                step += 1
        return step


if __name__ == '__main__':
    # Test Case 1
    num = 14
    print(Solution().numberOfSteps(num))  # 6

    # Test Case 2
    num = 8
    print(Solution().numberOfSteps(num))  # 4
