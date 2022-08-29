def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'

    result = {'Stuart': 0, 'Kevin': 0}
    for start in range(len(string)):
        if string[start] in vowels:
            result['Kevin'] += len(string) - start
        else:
            result['Stuart'] += len(string) - start

    if result['Stuart'] > result['Kevin']:
        print('Stuart', str(result['Stuart']))
    elif result['Stuart'] < result['Kevin']:
        print('Kevin', str(result['Kevin']))
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
