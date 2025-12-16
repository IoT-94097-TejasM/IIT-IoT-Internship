# Matrix 1: 3x4 as list of lists
mat1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Matrix 2: 3x4 as tuple of tuples
mat2 = (
    (12, 11, 10, 9),
    (8, 7, 6, 5),
    (4, 3, 2, 1)
)

def matrix_add_sub(m1, m2):
    add = []
    sub = []

    for i in range(3):
        add_row = []
        sub_row = []
        for j in range(4):
            add_row.append(m1[i][j] + m2[i][j])
            sub_row.append(m1[i][j] - m2[i][j])
        add.append(add_row)
        sub.append(sub_row)

    return add, sub


# -------- Main --------
addition, subtraction = matrix_add_sub(mat1, mat2)

print("Addition Matrix:")
for row in addition:
    print(row)

print("\nSubtraction Matrix:")
for row in subtraction:
    print(row)