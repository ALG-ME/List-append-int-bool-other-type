# Создание матрицы размера 3x3 и заполнение ее числами от 1 до 9
matrix_3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Создание любой матрицы, например, размера 2x4
matrix_custom = [[2, 4, 6, 8], [1, 3, 5, 7]]

# Вывод суммы всех элементов в матрице
sum_custom = sum(sum(row) for row in matrix_custom)
print(f'Сумма всех элементов в матрице:{sum_custom}')

# Вывод суммы элементов в каждой строке матрицы
row_sums_custom = [sum(row) for row in matrix_custom]
print(f'Сумма элементов в каждой строке матрицы: {row_sums_custom}')
