"""8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу."""


print('Введите элементы матрицы:')
matrix = []

for row in range(5):
    sum_row = 0
    matrix.append([])
    for col in range(5):
        if col < 4:
            el = int(input(f'{row + 1}-{col + 1}: '))
            matrix[row].append(el)
            sum_row += el
        else:
            matrix[row].append(sum_row)

for row in matrix:
    print(row)
