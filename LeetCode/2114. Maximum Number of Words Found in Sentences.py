from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(sentence.split()) for sentence in sentences])


if __name__ == '__main__':
    # Test Case 1
    sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    print(Solution().mostWordsFound(sentences))  # 6

    # Test Case 2
    sentences = ["please wait", "continue to fight", "continue to win"]
    print(Solution().mostWordsFound(sentences))  # 3
