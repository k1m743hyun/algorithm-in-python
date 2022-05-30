def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        li = []
        for s in list(string[i:i+k]):
            if s not in li:
                li.append(s)
        print(''.join(li))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)