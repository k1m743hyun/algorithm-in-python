matrix = [list(map(int, input().split())) for _ in range(9)]

max_val = 0
max_row, max_col = 0, 0
for row in range(9):
    for col in range(9):
        val = matrix[row][col]
        if val > max_val:
            max_val = val
            max_row, max_col = row, col

print(max_val)
print(max_row + 1, max_col + 1)
