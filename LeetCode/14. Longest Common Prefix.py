from collections import Counter

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''
        for p in zip(*strs):
            k, v = Counter(p).most_common(1)[0]
            if k == p[0] and v == len(p):
                common_prefix += k
            else:
                break
        return common_prefix