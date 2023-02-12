class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_dict = {}
        n = 96
        for i in list(key.replace(' ', '')):
            if i not in key_dict:
                n += 1
                key_dict[i] = chr(n)

        return ''.join([key_dict[j] if j != ' ' else j for j in message])


if __name__ == '__main__':
    # Test Case 1
    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    print(Solution().decodeMessage(key, message))  # this is a secret

    # Test Case 2
    key = "eljuxhpwnyrdgtqkviszcfmabo"
    message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
    print(Solution().decodeMessage(key, message))  # the five boxing wizards jump quickly
