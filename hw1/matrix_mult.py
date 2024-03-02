def matrix_mult(n, matrix_a, matrix_b):
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result

n = int(input())
matrix_a = []
for _ in range(n):
    matrix_a.append(list(map(int, input().split())))
matrix_b = []
for _ in range(n):
    matrix_b.append(list(map(int, input().split())))
result = matrix_mult(n, matrix_a, matrix_b)
for row in result:
    print(" ".join(map(str, row)))