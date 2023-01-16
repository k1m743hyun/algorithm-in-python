class Solution:
    def longestPalindrome(self, s: str) -> str:
        def extend(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result, extend(i, i + 1), extend(i, i + 2), key=len)

        return result


if __name__ == '__main__':
    # Test Case 1
    s = "babad"
    print(Solution().longestPalindrome(s))  # "bab"

    # Test Case 2
    s = "cbbd"
    print(Solution().longestPalindrome(s))  # "bb"
