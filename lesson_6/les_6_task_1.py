import sys
from memory_profiler import profile
from random import randint


@profile
def def_matrix(n):
    matrix = [[randint(0, 30) for _ in range(n)] for _ in range(n)]
    return matrix


@profile
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


@profile
def matrix_func_optimize(matrix):
    return max([min(col) for col in zip(*matrix)])


if __name__ == '__main__':
    print(sys.version, sys.platform)
    mtrx = def_matrix(1000)
    print(f'Matrix size: {sys.getsizeof(mtrx)} bytes')
    matrix_func_optimize(mtrx)


"""
3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] win32

Создаем матрицу 1000x1000:
mtrx = def_matrix(1000)
Размер mtrx = 8856 B (измерен sys.getsizeof(mtrx))

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    19     19.7 MiB     19.7 MiB           1   @profile
    20                                         def def_matrix(n):
    21     28.9 MiB   -312.3 MiB     1003003       matrix = [[randint(0, 30) for _ in range(n)] for _ in range(n)]
    22     28.9 MiB      0.0 MiB           1       return matrix


Передаем матрицу функции нахождения максимума среди минимумов каждого столбца:
matrix_func(mtrx)
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    24     29.0 MiB     29.0 MiB           1   @profile
    25                                         def matrix_func(matrix):
    26                                         
    27     29.0 MiB      0.0 MiB           1       row_mins = []
    28     29.1 MiB    -10.3 MiB        1001       for col in range(len(matrix[0])):
    29     29.1 MiB    -10.3 MiB        1000           min_el = matrix[0][col]
    30     29.1 MiB -10352.2 MiB     1001000           for row in range(len(matrix)):
    31     29.1 MiB -10341.8 MiB     1000000               if matrix[row][col] < min_el:
    32     29.1 MiB    -32.1 MiB        3028                   min_el = matrix[row][col]
    33     29.1 MiB    -10.4 MiB        1000           row_mins.append(min_el)
    34                                         
    35     29.0 MiB     -0.0 MiB           1       max_min = row_mins[0]
    36     29.0 MiB      0.0 MiB        1001       for el in row_mins:
    37     29.0 MiB      0.0 MiB        1000           if el > max_min:
    38                                                     max_min = el
    39     29.0 MiB      0.0 MiB           1       return max_min


Передаем матрицу оптимизированной функции нахождения максимума среди минимумов каждого столбца:
matrix_func_optimize(mtrx)
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    41     29.0 MiB     29.0 MiB           1   @profile
    42                                         def matrix_func_optimize(matrix):
    43     29.0 MiB      0.0 MiB        1003       return max([min(col) for col in zip(*matrix)])
    

Вторая реализация гораздо эффективнее по использованию памяти главным образом в связи с минимизацией
обходов матрицы циклами.
"""