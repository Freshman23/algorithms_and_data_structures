"""Найти максимальный элемент среди минимальных элементов столбцов квадратной матрицы.
Решение со встроенными функциями max() и min()."""


from random import randint
import cProfile


def def_matrix(n):
    matrix = [[randint(0, 30) for _ in range(n)] for _ in range(n)]
    return matrix


def matrix_func(matrix):

    row_mins = []
    for col in range(len(matrix[0])):
        col_lst = []
        for row in range(len(matrix)):
            col_lst.append(matrix[row][col])
        row_mins.append(min(col_lst))

    return max(row_mins)


# cur_matrix = def_matrix(4)
# print(cur_matrix)
# print(matrix_func(cur_matrix))

# cur_matrix = def_matrix(100)
# cProfile.run('matrix_func(cur_matrix)')
# 10306 function calls in 0.007 seconds
#     1    0.004    0.004    0.007    0.007 les_4_task_1b.py:14(matrix_func)
#   101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#   100    0.000    0.000    0.000    0.000 {built-in method builtins.min}
# 10100    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}

# cur_matrix = def_matrix(200)
# cProfile.run('matrix_func(cur_matrix)')
# 40606 function calls in 0.017 seconds
#     1    0.011    0.011    0.017    0.017 les_4_task_1b.py:14(matrix_func)
#   201    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#   200    0.001    0.000    0.001    0.000 {built-in method builtins.min}
# 40200    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}

# "import les_4_task_1b;matrix = les_4_task_1b.def_matrix(10)" "les_4_task_1b.matrix_func(matrix)"
# 1000 loops, best of 5: 18.2 usec per loop

# "import les_4_task_1b;matrix = les_4_task_1b.def_matrix(20)" "les_4_task_1b.matrix_func(matrix)"
# 1000 loops, best of 5: 59 usec per loop

# "import les_4_task_1b;matrix = les_4_task_1b.def_matrix(50)" "les_4_task_1b.matrix_func(matrix)"
# 1000 loops, best of 5: 363 usec per loop

# "import les_4_task_1b;matrix = les_4_task_1b.def_matrix(100)" "les_4_task_1b.matrix_func(matrix)"
# 1000 loops, best of 5: 1.31 msec per loop

# "import les_4_task_1b;matrix = les_4_task_1b.def_matrix(200)" "les_4_task_1b.matrix_func(matrix)"
# 1000 loops, best of 5: 5.03 msec per loop
