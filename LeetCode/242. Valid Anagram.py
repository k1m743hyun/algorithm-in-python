from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        else:
            return False


if __name__ == '__main__':
    # Test Case 1
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))  # true

    # Test Case 2
    s = "rat"
    t = "car"
    print(Solution().isAnagram(s, t))  # true
