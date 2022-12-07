spot = []
for left_x, bottom_y in [tuple(map(int, input().split())) for _ in range(int(input()))]:
    spot += [(x, y) for y in range(bottom_y, bottom_y + 10) for x in range(left_x, left_x + 10)]

print(len(set(spot)))
