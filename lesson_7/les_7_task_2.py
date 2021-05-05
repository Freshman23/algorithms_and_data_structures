""" 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random

array = [round(random.uniform(0, 50), 3) for _ in range(10)]
print(f'{array} - исходный массив')


def merge_sort_asc(arr: list):

    if len(arr) <= 1:
        return

    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]

    merge_sort_asc(left)
    merge_sort_asc(right)

    common = []
    le = 0
    ri = 0

    while le < len(left) and ri < len(right):
        if left[le] <= right[ri]:
            common.append(left[le])
            le += 1
        else:
            common.append(right[ri])
            ri += 1

    while le < len(left):
        common.append(left[le])
        le += 1

    while ri < len(right):
        common.append(right[ri])
        ri += 1

    for i in range(len(arr)):
        arr[i] = common[i]


merge_sort_asc(array)
print(f'{array} - упорядоченный по возрастанию массив')
