class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    # Test Case 1
    x = 121
    print(Solution().isPalindrome(x))  # true

    # Test Case 2
    x = -121
    print(Solution().isPalindrome(x))  # false

    # Test Case 3
    x = 10
    print(Solution().isPalindrome(x))  # false
