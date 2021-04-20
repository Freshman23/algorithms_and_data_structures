"""7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться."""


from random import randint


array = [randint(0, 20) for _ in range(10)]
print(array)

if array[0] < array[1]:
    min_1 = array[0]
    min_2 = array[1]
else:
    min_1 = array[1]
    min_2 = array[0]

for num in array[2:]:
    if num <= min_1:
        min_2 = min_1
        min_1 = num
    elif min_1 < num <= min_2:
        min_2 = num
print(f'Два наименьших элемента из данного массива: {min_1}, {min_2}')
