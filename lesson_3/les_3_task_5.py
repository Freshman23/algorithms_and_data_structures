"""5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве."""


from random import randint


array = [randint(-100, 100) for _ in range(30)]
print(array)

"""Так как элементов с максимальным отрицательным значением может быть несколько,
создадим пустой список для добавления, возможно, нескольких индексов"""
ind_max_negative = []
max_negative = -101
for ind, num in enumerate(array):
    if max_negative < num < 0:
        max_negative = num
        ind_max_negative = [ind]
    elif max_negative == num:
        ind_max_negative.append(ind)
print(f'Максимальное отрицательное значение равно {max_negative} элемента на позиции {ind_max_negative}')
