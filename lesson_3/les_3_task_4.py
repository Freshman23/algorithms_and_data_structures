"""4. Определить, какое число в массиве встречается чаще всего."""


from random import randint


array = [randint(0, 10) for _ in range(50)]
print(array)

"""Создаем словарь с ключами - уникальными числами массива,
   значениями - количеством вхождений этого числа в массив"""
occurs = {}
for num in array:
    if num in occurs.keys():
        occurs[num] += 1
    else:
        occurs.update({num: 1})
print(occurs)

"""Находим число/числа с максимальным количеством вхождений в данный массив"""
max_occurs = 0
nums_max_occurs = []
for key, value in occurs.items():
    if value > max_occurs:
        max_occurs = value
        nums_max_occurs = [key]
    elif value == max_occurs:
        nums_max_occurs.append(key)
print(f'В данном массиве чаще всего ({max_occurs} раз) встречается число/числа: {nums_max_occurs}')
