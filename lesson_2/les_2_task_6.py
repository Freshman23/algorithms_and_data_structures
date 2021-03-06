"""6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать
не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше
введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ."""


from random import randint

rand_num = randint(0, 100)
print('Угадайте целое число от 0 до 100. Дается 10 попыток.')

for i in range(10):
    answer = int(input(f'{i + 1}-я попытка: '))
    if answer < rand_num:
        print('Загаданное число больше вашего.')
    elif answer > rand_num:
        print('Загаданное число меньше вашего.')
    else:
        print(f'Поздравляю! Вы угадали. Это число: {answer}')
        break
    if i == 9:
        print(f'Попытки закончились. Вы не угадали. Это было число: {rand_num}')

print('Игра завершена.')
