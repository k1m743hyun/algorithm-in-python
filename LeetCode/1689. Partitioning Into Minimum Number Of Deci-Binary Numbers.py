class Solution:
    def minPartitions(self, n: str) -> int:
        return max(list(n))


if __name__ == '__main__':
    # Test Case 1
    n = "32"
    print(Solution().minPartitions(n))  # 3

    # Test Case 2
    n = "82734"
    print(Solution().minPartitions(n))  # 8

    # Test Case 3
    n = "27346209830709182346"
    print(Solution().minPartitions(n))  # 9
