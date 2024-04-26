def rotate_matrix(matrix)
    # Получаем размеры исходной матрицы
    n = len(matrix)
    m = len(matrix[0])

    # Создаем новую матрицу с размерами m x n
    rotated_matrix = [[0]  n for _ in range(m)]

    # Заполняем новую матрицу
    for i in range(n)
        for j in range(m)
            # Транспонируем координаты и инвертируем порядок элементов в строке
            rotated_matrix[j][n - i - 1] = matrix[i][j]

    return rotated_matrix
    
# Чтение входных данных
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Поворот матрицы на 90 градусов
rotated_matrix = rotate_matrix(matrix)
print(Вывод)
# Вывод результата
for row in rotated_matrix
    print(row )
