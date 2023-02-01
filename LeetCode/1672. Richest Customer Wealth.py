from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(account) for account in accounts])


if __name__ == '__main__':
    # Test Case 1
    accounts = [[1, 2, 3], [3, 2, 1]]
    print(Solution().maximumWealth(accounts))  # 6

    # Test Case 2
    accounts = [[1, 5], [7, 3], [3, 5]]
    print(Solution().maximumWealth(accounts))  # 10
