"""1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел
в диапазоне от 2 до 9. Примечание: 8 разных ответов."""


multiplicity = {}

for digit in range(2, 10):
    for num in range(2, 100):
        if num % digit == 0:
            if digit in multiplicity.keys():
                multiplicity[digit] += 1
            else:
                multiplicity.update({digit: 1})

print('Числа в диапазоне от 2 до 99 включительно кратны цифрам:')
for key, value in multiplicity.items():
    print(f'"{key}" - {value} раз')
