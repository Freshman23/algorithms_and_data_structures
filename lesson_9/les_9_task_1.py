""" Задание №1.
    Определение количества различных подстрок с использованием хеш-функции.
    Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
    Примечания:
    * в сумму не включаем пустую строку и строку целиком;
    * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib
    задача считается не решённой.
"""

from hashlib import sha1


def subs_counter(s: str, subs: str) -> int:
    assert len(s) > 0 and len(subs) > 0, 'Длины строки и подстроки должны быть больше 0'
    assert len(s) > len(subs), 'Длина подстроки должна быть меньше длины строки'

    len_sub = len(subs)
    hash_sub = sha1(subs.encode('utf-8')).hexdigest()
    subs_cnt = 0

    for i in range(len(s) - len_sub + 1):
        if hash_sub == sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
            subs_cnt += 1

    return subs_cnt


my_str = input('Введите строку: ')
my_substr = input('Введите подстроку: ')
amount = subs_counter(my_str, my_substr)

print(f'Подстрока в строке встречается {amount} раз.' if amount != 0 else 'Подстрока не встречается.')
