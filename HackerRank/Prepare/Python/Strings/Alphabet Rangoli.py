def print_rangoli(size):
    # your code goes here
    for s in range(size):
        c = ord('a') + size - s - 1
        print('-'.join([chr(j) for j in range(c + s, c - 1, -1)] + [chr(k) for k in range(c + 1, c + s + 1)]).center((size - 1) * 4 + 1, '-'))
    for s in range(size - 2, -1, -1):
        c = ord('a') + size - s - 1
        print('-'.join([chr(j) for j in range(c + s, c - 1, -1)] + [chr(k) for k in range(c + 1, c + s + 1)]).center((size - 1) * 4 + 1, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)