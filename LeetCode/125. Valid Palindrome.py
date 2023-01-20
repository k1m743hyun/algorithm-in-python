import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined = ''.join(re.compile(r'[A-Za-z0-9]+').findall(s)).lower()
        return refined == refined[::-1]

if __name__ == '__main__':
    # Test Case 1
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome(s)) # true

    # Test Case 2
    s = "race a car"
    print(Solution().isPalindrome(s)) # false

    # Test Case 3
    s = " "
    print(Solution().isPalindrome(s)) # true