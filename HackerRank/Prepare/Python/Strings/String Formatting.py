def print_formatted(number):
    # your code goes here
    num_list = [[str(i + 1), str(oct(i + 1)).replace('0o', ''),
                 str(hex(i + 1)).replace('0x', ''),
                 str(bin(i + 1)).replace('0b', '')]
                for i in range(number)]
    d_list, o_list, h_list, b_list = zip(*num_list)

    s = len(b_list[-1])
    for i in range(number):
        print(d_list[i].rjust(s, ' '),
              o_list[i].rjust(s, ' '),
              h_list[i].rjust(s, ' ').upper(),
              b_list[i].rjust(s, ' '), sep=' ')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
