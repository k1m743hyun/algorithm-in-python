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


if __name__ == '__main__':
    # Test Case 1
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))  # 3

    # Test Case 2
    s = "bbbbb"
    print(Solution().lengthOfLongestSubstring(s))  # 1

    # Test Case 3
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))  # 3
