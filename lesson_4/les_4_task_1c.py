"""Найти максимальный элемент среди минимальных элементов столбцов квадратной матрицы.
Короткое решение со встроенными функциями zip(), max() и min().
Однозначно это решение наиболее эффективное: максимально лаконичное и быстрое в исполнении."""


from random import randint
import cProfile


def def_matrix(n):
    matrix = [[randint(0, 30) for _ in range(n)] for _ in range(n)]
    return matrix


def matrix_func(matrix):
    return max([min(col) for col in zip(*matrix)])


# cur_matrix = def_matrix(4)
# print(cur_matrix)
# print(matrix_func(cur_matrix))

# cur_matrix = def_matrix(100)
# cProfile.run('matrix_func(cur_matrix)')
# 106 function calls in 0.001 seconds
#   1    0.000    0.000    0.001    0.001 les_4_task_1c.py:14(matrix_func)
#   1    0.000    0.000    0.001    0.001 les_4_task_1c.py:15(<listcomp>)
#   1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
# 100    0.000    0.000    0.000    0.000 {built-in method builtins.min}

# cur_matrix = def_matrix(200)
# cProfile.run('matrix_func(cur_matrix)')
# 206 function calls in 0.001 seconds
#   1    0.000    0.000    0.001    0.001 les_4_task_1c.py:14(matrix_func)
#   1    0.000    0.000    0.001    0.001 les_4_task_1c.py:15(<listcomp>)
#   1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
# 200    0.001    0.000    0.001    0.000 {built-in method builtins.min}

# "import les_4_task_1c;matrix = les_4_task_1c.def_matrix(10)" "les_4_task_1c.matrix_func(matrix)"
# 1000 loops, best of 5: 4.76 usec per loop

# "import les_4_task_1c;matrix = les_4_task_1c.def_matrix(20)" "les_4_task_1c.matrix_func(matrix)"
# 1000 loops, best of 5: 13 usec per loop

# "import les_4_task_1c;matrix = les_4_task_1c.def_matrix(50)" "les_4_task_1c.matrix_func(matrix)"
# 1000 loops, best of 5: 61.3 usec per loop

# "import les_4_task_1c;matrix = les_4_task_1c.def_matrix(100)" "les_4_task_1c.matrix_func(matrix)"
# 1000 loops, best of 5: 226 usec per loop

# "import les_4_task_1c;matrix = les_4_task_1c.def_matrix(200)" "les_4_task_1c.matrix_func(matrix)"
# 1000 loops, best of 5: 902 usec per loop
