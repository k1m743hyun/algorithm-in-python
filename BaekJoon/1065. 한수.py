def validNum(num):
    num_list = list(map(int, list(str(num))))

    flag = True
    pro_d = num_list[1] - num_list[0]
    for i in range(2, len(num_list)):
        d = num_list[i] - num_list[i - 1]
        if d != pro_d:
            flag = False
            break

    return flag


def countNum(num):
    if num < 100:
        return num

    cnt = 99
    for n in range(100, num + 1):
        if validNum(n):
            cnt += 1

    return cnt


if __name__ == '__main__':
    print(countNum(int(input())))
