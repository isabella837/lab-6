# Personalized values (MUST INCLUDE)
d1 = 5
d2 = 6
k = (d1 + d2) % 4 + 2
shift = d1 - d2
rows_keep = (d1 % 2) + 2

# Component A: Create grid
grid = [
    [10, 12, 14, 16],
    [18, 20, 22, 24],
    [26, 28, 30, 32]
]

print("FULL MATRIX:")
for row in grid:
    print(row)

# One specific element (example: row 1, col 2)
print("\nONE ELEMENT [1][2]:", grid[1][2])

# First two rows
print("\nFIRST TWO ROWS:")
for row in grid[:2]:
    print(row)

# First column
print("\nFIRST COLUMN:")
for row in grid:
    print(row[0])

# 2x2 sub-array from upper-left
print("\n2x2 SUB_ARRAY:")
for row in grid[:2]:
    print(row[:2])

# Component B: ID-based modification
rows = len(grid)
cols = len(grid[0])

row_index = d1 % rows
col_index = d2 % cols

print("\nRow to modify:", row_index)
print("Column to modify:", col_index)

# Print before modification
print("\nMATRIX BEFORE MODIFICATION:")
for row in grid:
    print(row)

# Add shift to row
for j in range(cols):
    grid[row_index][j] += shift

# Multiply column by k
for i in range(rows):
    grid[i][col_index] *= k

# Print after modification
print("\nMATRIX AFTER MODIFICATION:")
for row in grid:
    print(row)

# Sub-array (rows_keep & k)
print("\nSUB-ARRAY (rows_keep & k):")
for row in grid[:rows_keep]:
    print(row[:k]) # k > cols --> Python automatically stops at max columns

    
















        

                 






