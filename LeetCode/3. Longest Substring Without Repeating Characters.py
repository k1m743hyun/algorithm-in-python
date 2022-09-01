class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        li = []
        for val in s:
            if val in li:
                li = li[li.index(val) + 1:]

            li.append(val)

            if max_len < len(li):
                max_len = len(li)

        return max_len
