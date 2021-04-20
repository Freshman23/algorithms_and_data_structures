"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""


from random import randint


array = [randint(0, 100) for _ in range(10)]
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

array[min_ind], array[max_ind] = array[max_ind], array[min_ind]
print(array)
