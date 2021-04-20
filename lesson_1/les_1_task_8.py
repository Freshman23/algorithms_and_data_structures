"""8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)."""

print('Ведите три разных целых числа:')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a in range(b, c) or a in range(c, b):
    print('Среднее число:', a)
elif b in range(a, c) or b in range(c, a):
    print('Среднее число:', b)
else:
    print('Среднее число:', c)
