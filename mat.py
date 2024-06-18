def input_matrix_elements():
    matrices = []
    for i in range(2):
        rows = int(input(f"Enter the number of rows for matrix {i + 1}: "))
        cols = int(input(f"Enter the number of columns for matrix {i + 1}: "))
        matrix = []
        print(f"Enter elements for matrix {i + 1}:")
        for _ in range(rows):
            row = [int(x) for x in input().split()]
            if len(row) != cols:
                print("Error: Number of elements in the row should match the number of columns.")
                return []
            matrix.append(row)
        matrices.append(matrix)
    return matrices

def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error: Matrices should have the same dimensions for addition.")
        return []
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Error: Number of columns in the first matrix should be equal to the number of rows in the second matrix for multiplication.")
        return []
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    return result

def display_result(result):
    print("Resultant matrix:")
    for row in result:
        print(' '.join(map(str, row)))

# Main program
matrix1 = input_matrix_elements()
matrix2 = input_matrix_elements()

if matrix1 and matrix2:
    result_addition = matrix_addition(matrix1, matrix2)
    result_multiplication = matrix_multiplication(matrix1, matrix2)

    if result_addition:
        print("\nMatrix Addition:")
        display_result(result_addition)

    if result_multiplication:
        print("\nMatrix Multiplication:")
        display_result(result_multiplication)
