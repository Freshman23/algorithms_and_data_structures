"""9. Найти максимальный элемент среди минимальных элементов столбцов матрицы."""


from random import randint


rows = 10
cols = 10
matrix = [[randint(0, 30) for col in range(cols)] for row in range(rows)]
print('Матрица:')
for row in matrix:
    print(row)

row_mins = []
for col in range(cols):
    min_el = matrix[0][col]
    for row in range(rows):
        if matrix[row][col] < min_el:
            min_el = matrix[row][col]
    row_mins.append(min_el)
print()
print(row_mins, '- минимальные элементы в каждом столбце.')

max_min = row_mins[0]
for el in row_mins:
    if el > max_min:
        max_min = el
print(max_min, '- максимальный из минимальных элементов каждого столбца.')
