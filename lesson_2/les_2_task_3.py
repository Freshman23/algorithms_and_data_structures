"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, надо вывести 6843."""


number = input('Введите натуральное число: ')
reverse = ''
for num in number:
    reverse = num + reverse
print('Обратная последовательность введенного числа:', reverse)
