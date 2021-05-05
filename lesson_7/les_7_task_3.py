""" 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
то используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""

import random

array = [random.randint(0, 100) for _ in range(11)]
print(f'{array} - исходный массив')


def find_median(arr: list):
    cur_arr = arr[:]
    j = 0

    while j <= len(cur_arr) // 2:
        min_ind = j

        for i in range(j + 1, len(arr)):
            if cur_arr[i] < cur_arr[min_ind]:
                min_ind = i

        cur_arr[j], cur_arr[min_ind] = cur_arr[min_ind], cur_arr[j]
        j += 1

    print(f'{cur_arr[:j - 1]} <= {cur_arr[j - 1]} <= {cur_arr[j:]} '
          f'- меньшая и большая части массива относительно медианы.')

    return cur_arr[j - 1]


print(f'Медиана: {find_median(array)}')