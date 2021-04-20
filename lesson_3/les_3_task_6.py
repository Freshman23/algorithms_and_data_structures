"""6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать."""


from random import randint


array = [randint(0, 20) for _ in range(10)]
print(array)

min_ind = 0
max_ind = 0
min_num = array[0]
max_num = array[0]

for ind, num in enumerate(array):
    if num < min_num:
        min_num = num
        min_ind = ind
    elif num > max_num:
        max_num = num
        max_ind = ind
print(f'Минимум - {min_num}, Максимум - {max_num}')

del array[min_ind], array[max_ind if min_ind > max_ind else max_ind - 1]

sum_mid = 0
for num in array:
    sum_mid += num
print(f'Сумма чисел массива без максимального и минимального элемента = {sum_mid}')
