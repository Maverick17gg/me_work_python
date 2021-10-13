matrix_1 = [[1, 2, 3],
            [10, 15, 5],
            [4, 8, 9]]
matrix_2 = [[5, 4, 7],
            [11, 23, 3],
            [17, 2, 6]]

matrix_3 = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

matrix_len = len(matrix_1)
for matrix in range(len(matrix_1)):
    for matrix1 in range(len(matrix_2)):
        matrix_3[matrix][matrix1] = matrix_1[matrix][matrix1] * matrix_2[matrix][matrix1]
print(matrix_3)
