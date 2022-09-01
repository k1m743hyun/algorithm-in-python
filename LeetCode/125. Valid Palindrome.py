import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined = ''.join(re.compile(r'[A-Za-z0-9]+').findall(s)).lower()
        return refined == refined[::-1]
