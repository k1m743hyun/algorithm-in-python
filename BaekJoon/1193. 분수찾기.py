x = int(input())

num = 0
step = 1
while True:
    num += step
    if num >= x:
        break
    step += 1

if step % 2 == 0:
    print('{}/{}'.format(x - (num - step), step - (x - (num - step)) + 1))
else:
    print('{}/{}'.format(step - (x - (num - step)) + 1, x - (num - step)))
