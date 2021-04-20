"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""

from collections import deque
from functools import reduce


def conv_hex_dec(hex_arr):
    dec_arr = []
    conv_dct = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    for digit in hex_arr:
        if digit in ['a', 'b', 'c', 'd', 'e', 'f']:
            digit = digit.upper()
        dec_arr.append(conv_dct[digit])

    return dec_arr


def conv_dec_hex(dec_arr):
    hex_arr = []
    conv_tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

    for digit in dec_arr:
        hex_arr.append(conv_tuple[digit])

    return hex_arr


def addition(hex_num_1, hex_num_2):
    hex_num_1 = deque(hex_num_1)
    hex_num_2 = deque(hex_num_2)
    hex_num_1.reverse()
    hex_num_2.reverse()

    if len(hex_num_1) < len(hex_num_2):
        hex_num_1, hex_num_2 = hex_num_2, hex_num_1
    hex_num_1 += [0]
    hex_num_2 += [0] * (len(hex_num_1) - len(hex_num_2))

    sum_num = deque()
    next_rank = 0
    for rank in range(len(hex_num_1)):
        sum_num.append((hex_num_1[rank] + hex_num_2[rank] + next_rank) % 16)
        next_rank = (hex_num_1[rank] + hex_num_2[rank] + next_rank) // 16

    sum_num.reverse()

    while sum_num[0] == 0 and len(sum_num) > 1:
        del sum_num[0]

    return list(sum_num)


def multiplication(hex_num_1, hex_num_2):
    hex_num_1 = deque(hex_num_1)
    hex_num_2 = deque(hex_num_2)
    hex_num_1.reverse()
    hex_num_2.reverse()

    premultiplication_lst = []
    for ind, multiplier in enumerate(hex_num_1):
        term = deque()
        next_rank = 0
        for rank in hex_num_2:
            term.append((multiplier * rank + next_rank) % 16)
            next_rank = (multiplier * rank + next_rank) // 16
        if next_rank != 0:
            term.append(next_rank)
        term.extendleft([0] * ind)
        term.reverse()
        premultiplication_lst.append(list(term))

    multiplication_num = reduce(addition, premultiplication_lst)

    while multiplication_num[0] == 0 and len(multiplication_num) > 1:
        del multiplication_num[0]

    return multiplication_num


while True:
    answer = input('To continue push [Enter], to quit type "quit" and push [Enter]: ')
    if answer == "quit":
        break
    a = list(input('Enter hexadecimal number #1: '))
    b = list(input('Enter hexadecimal number #2: '))
    add_a_b = conv_dec_hex(addition(conv_hex_dec(a), conv_hex_dec(b)))
    multi_a_b = conv_dec_hex(multiplication(conv_hex_dec(a), conv_hex_dec(b)))
    print(f"The result of adding these numbers: {''.join(add_a_b)}\n"
          f"The result of multiplying these numbers: {''.join(multi_a_b)}\n"
          f"{'*' * (42 + len(multi_a_b))}")
