"""3. Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ."""

import random

print('Введите границы числового и буквенного диапазона:')
low = int(input('Нижняя граница числового диапазона: '))
high = int(input('Верхняя граница числового диапазона: '))
c_low = input('Нижняя граница буквенного диапазона: ')
c_high = input('Верхняя граница буквенного диапазона: ')

rand_int_num = random.randint(low, high)
rand_float_num = random.uniform(low, high)
rand_char = chr(random.randint(ord(c_low), ord(c_high)))

print(f'Случайное целое число из заданного числового диапазона: {rand_int_num}\n'
      f'Случайное вещественное число из заданного числового диапазона: {rand_float_num}\n'
      f'Случайная буква из заданного буквенного диапазона: {rand_char}')
