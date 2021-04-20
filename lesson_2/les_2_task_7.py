"""7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел
выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число."""


def prove_equal(n):
    summa = 0
    for num in range(1, n + 1):
        summa += num
    if summa == n * (n + 1) / 2:
        return f'Равенство: 1+2+...+n = n(n+1)/2, при n = {n} - верно.'
    return f'Равенство: 1+2+...+n = n(n+1)/2, при n = {n} - не верно.'


print(prove_equal(1))
print(prove_equal(10))
print(prove_equal(100))
print(prove_equal(1000))
