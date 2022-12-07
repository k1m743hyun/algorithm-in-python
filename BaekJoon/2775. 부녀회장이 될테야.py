t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    apt = []
    for floor_num in range(k+1):
        floor = []
        for room_num in range(n):
            if floor_num == 0:
                floor.append(room_num+1)
            else:
                floor.append(sum(apt[floor_num - 1][:room_num+1]))
        apt.append(floor)

    print(apt[k][n-1])
