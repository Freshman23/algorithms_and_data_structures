"""Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа
должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
"""


import cProfile


def sieve(n):
    """Первый способ — с помощью алгоритма «Решето Эратосфена»."""
    prime_nums = [2]
    i = 1
    cur_num = 3

    while i < n:
        for ind, num in enumerate(prime_nums[:]):
            if cur_num % num == 0:
                cur_num += 1
                break
            elif ind == len(prime_nums) - 1:
                prime_nums.append(cur_num)
                i += 1
                cur_num += 1

    return prime_nums[n - 1]


def prime(n):
    """Второй способ — оптимизиорванный алгоритм с использованием «Решето Эратосфена» и некоторых утверждений."""
    prime_nums = [2, 3, 5, 7]
    i = 4
    cur_num = 11

    while i < n:
        for num in prime_nums[1:]:
            if num > cur_num ** 0.5:
                prime_nums.append(cur_num)
                i += 1
                cur_num += 2
                break
            elif cur_num % num == 0:
                cur_num += 2
                break

    return prime_nums[n - 1]


# print(sieve(1000))
# print(prime(1000))

# cProfile.run('sieve(100)')
# 5408 function calls in 0.006 seconds
#    1    0.004    0.004    0.005    0.005 les_4_task_2.py:28(sieve)
# 5305    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#   99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('prime(100)')
# 100 function calls in 0.001 seconds
# 1    0.000    0.000    0.001    0.001 les_4_task_2.py:46(prime)
# 96    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('sieve(500)')
# 128979 function calls in 0.090 seconds
#      1    0.070    0.070    0.090    0.090 les_4_task_2.py:10(sieve)
# 128476    0.020    0.000    0.020    0.000 {built-in method builtins.len}
#    499    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('prime(500)')
# 500 function calls in 0.007 seconds
# 1    0.007    0.007    0.007    0.007 les_4_task_2.py:29(prime)
# 496    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# "les_4_task_2.sieve(50)"
# 100 loops, best of 5: 396 usec per loop

# "les_4_task_2.prime(50)"
# 100 loops, best of 5: 133 usec per loop

# "les_4_task_2.sieve(100)"
# 100 loops, best of 5: 1.16 msec per loop

# "les_4_task_2.prime(100)"
# 100 loops, best of 5: 417 usec per loop

# "les_4_task_2.sieve(200)"
# 100 loops, best of 5: 4.54 msec per loop

# "les_4_task_2.prime(200)"
# 100 loops, best of 5: 1.21 msec per loop

# "les_4_task_2.sieve(500)"
# 100 loops, best of 5: 31.3 msec per loop

# "les_4_task_2.prime(500)"
# 100 loops, best of 5: 5.29 msec per loop

# "les_4_task_2.prime(1000)"
# 100 loops, best of 5: 16.1 msec per loop

# "les_4_task_2.prime(10000)"
# 1 loop, best of 1: 1.17 sec per loop

# "les_4_task_2.prime(100000)"
# 1 loop, best of 1: 197 sec per loop

"""Очевидно второй способ гораздо быстрее и эффективнее со сложностью O(n**3/2)"""
