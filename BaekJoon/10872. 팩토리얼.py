import sys


def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(factorial(n))
