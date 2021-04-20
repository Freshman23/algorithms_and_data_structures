"""Найти максимальный элемент среди минимальных элементов столбцов квадратной матрицы.
Решение без встроенных функций max() и min()."""


from random import randint
import cProfile


def def_matrix(n):
    matrix = [[randint(0, 30) for _ in range(n)] for _ in range(n)]
    return matrix


def matrix_func(matrix):

    row_mins = []
    for col in range(len(matrix[0])):
        min_el = matrix[0][col]
        for row in range(len(matrix)):
            if matrix[row][col] < min_el:
                min_el = matrix[row][col]
        row_mins.append(min_el)

    max_min = row_mins[0]
    for el in row_mins:
        if el > max_min:
            max_min = el
    return max_min


# cur_matrix = def_matrix(4)
# print(cur_matrix)
# print(matrix_func(cur_matrix))

# cur_matrix = def_matrix(100)
# cProfile.run('matrix_func(cur_matrix)')
# 205 function calls in 0.001 seconds
#   1    0.001    0.001    0.001    0.001 les_4_task_1a.py:13(matrix_func)
# 101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cur_matrix = def_matrix(200)
# cProfile.run('matrix_func(cur_matrix)')
# 405 function calls in 0.003 seconds
#   1    0.003    0.003    0.003    0.003 les_4_task_1a.py:13(matrix_func)
# 201    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 200    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# "import les_4_task_1a;matrix = les_4_task_1a.def_matrix(10)" "les_4_task_1a.matrix_func(matrix)"
# 1000 loops, best of 5: 11.4 usec per loop

# "import les_4_task_1a;matrix = les_4_task_1a.def_matrix(20)" "les_4_task_1a.matrix_func(matrix)"
# 1000 loops, best of 5: 35.6 usec per loop

# "import les_4_task_1a;matrix = les_4_task_1a.def_matrix(50)" "les_4_task_1a.matrix_func(matrix)"
# 1000 loops, best of 5: 203 usec per loop

# "import les_4_task_1a;matrix = les_4_task_1a.def_matrix(100)" "les_4_task_1a.matrix_func(matrix)"
# 1000 loops, best of 5: 753 usec per loop

# "import les_4_task_1a;matrix = les_4_task_1a.def_matrix(200)" "les_4_task_1a.matrix_func(matrix)"
# 1000 loops, best of 5: 2.79 msec per loop
