for _ in range(int(input())):
    h, w, n = map(int, input().split())

    hotel = [[0] * w] * h

    people = 0
    for room in range(w):
        for floor in range(h):
            hotel[floor][room] = 1
            people += 1

            if people == n:
                print((floor + 1) * 100 + (room + 1))
