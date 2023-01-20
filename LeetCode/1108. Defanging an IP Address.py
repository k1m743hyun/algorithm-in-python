class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


if __name__ == '__main__':
    # Test Case 1
    address = "1.1.1.1"
    print(Solution().defangIPaddr(address))  # 1[.]1[.]1[.]1

    # Test Case 2
    address = "255.100.50.0"
    print(Solution().defangIPaddr(address))  # 255[.]100[.]50[.]0
