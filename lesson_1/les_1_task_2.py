"""2. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
проходящей через эти точки."""

print('Введите координаты двух точек целыми числами:')
x_1 = int(input('x_1: '))
y_1 = int(input('y_1: '))
x_2 = int(input('x_2: '))
y_2 = int(input('y_2: '))

if y_1 == y_2:
    print(f'Уравнение прямой: y={y_1}')
elif x_1 == x_2:
    print(f'Уравнение прямой: x={x_1}')
else:
    k = round((y_2 - y_1) / (x_2 - x_1), 3)
    b = round((y_1 * x_2 - y_2 * x_1) / (x_2 - x_1), 3)
    if b > 0:
        print(f'Уравнение прямой: y={k}x+{b}')
    elif b < 0:
        print(f'Уравнение прямой: y={k}x{b}')
    else:
        print(f'Уравнение прямой: y={k}x')
