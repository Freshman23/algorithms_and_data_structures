"""5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква."""

number = int(input('Введите номер буквы в алфавите (от 1 до 26): '))

print(f'Буква в алфавите под номером {number} - "{chr(number + 96)}".')
