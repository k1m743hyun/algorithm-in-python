class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('(al)', 'al').replace('()', 'o')


if __name__ == '__main__':
    # Test Case 1
    command = "G()(al)"
    print(Solution().interpret(command))  # Goal

    # Test Case 2
    command = "G()()()()(al)"
    print(Solution().interpret(command))  # Gooooal

    # Test Case 3
    command = "(al)G(al)()()G"
    print(Solution().interpret(command))  # alGalooG
