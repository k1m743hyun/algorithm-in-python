class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_dict = {}
        n = 96
        for i in list(key.replace(' ', '')):
            if i not in key_dict:
                n += 1
                key_dict[i] = chr(n)

        return ''.join([key_dict[j] if j != ' ' else j for j in message])
