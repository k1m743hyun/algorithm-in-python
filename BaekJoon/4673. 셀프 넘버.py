def d(n):
    return n + sum(map(int, list(str(n))))


if __name__ == '__main__':
    total = list(range(10000))
    for v in sorted(set(total) - set(list(d(num) for num in total))):
        print(v)
