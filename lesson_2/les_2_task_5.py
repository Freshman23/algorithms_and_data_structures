"""5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м
включительно. Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке."""


table = ''
for code in range(32, 128):
    if (code - 1) % 10 == 0:
        table += f'{code:3}: {chr(code)}\n'
    else:
        table += f'{code:3}: {chr(code)}   '
print(table)
