import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined = ''.join(re.compile(r'[A-Za-z0-9]+').findall(s)).lower()

        flag = True
        for idx, val in enumerate(refined):
            if idx > len(refined) // 2:
                break

            if val != refined[len(refined) - idx - 1]:
                flag = False
                break

        return flag
