"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""


amount_mems = int(input('Введите количество чисел в последовательности: '))
max_sum = 0
max_mem = ''

for i in range(amount_mems):
    mem = input(f'Введите {i + 1}-е число: ')
    sum_mem = 0
    for digit in mem:
        sum_mem += int(digit)
    if sum_mem > max_sum:
        max_sum = sum_mem
        max_mem = mem

print(f'Первое число "{max_mem}" из введенных с максимальной суммой цифр, равной {max_sum}.')
