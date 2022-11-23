n = input()

if len(n) == 1:
    n = '0' + n
n_list = list(n)

step = 0
temp = '00'
while True:
    step += 1
    temp = n_list[-1] + str(sum(map(int, n_list)))[-1]
    if temp == n:
        break
    n_list = list(temp)

print(step)
