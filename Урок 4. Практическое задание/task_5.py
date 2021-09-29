"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000

Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""
from timeit import repeat, default_timer

def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

def simple_2(i):
    rang = i**2
    res = [1]
    sieve = set(range(2, rang+1))
    while sieve:
        prime = min(sieve)
        res.append(prime)
        sieve -= set(range(prime, rang+1, prime))
        # print(sieve)
    return res[i]

def simple_3(i):
    '''
    Создаем массив НЕпростых чисел = False, затем пробегаем по ним кратностями 2 3 4 5 6
    критерий оптимальности алгоритма состоит в дальнейшем его совершенствовании путем
    исключения лишних вычислений (прогонов кратных 2 3 4 5...)... но на это нет уже времени...
    '''
    rang = i**2
    sieve = [False for x in range(rang)]
    for idx in range(2, rang):
        for x in range(idx, rang, idx):
            sieve[x] = idx if not sieve[x] else sieve[x]
        # print(len(sieve), sorted(list(set(sieve))))
    return sorted(list(set(sieve)))[i]

i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple_2(i))
i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple_3(i))

statement = ['simple(10)','simple(100)','simple(1000)',
             'simple_2(10)', 'simple_2(100)', 'simple_2(300)',
             'simple_3(10)', 'simple_3(100)', 'simple_3(1000)']

for st in statement:
    print(f'{st:<15} {min(repeat(stmt=st, globals=globals(), repeat=1, number=10)):>10.5f}')

'''
Введите порядковый номер искомого простого числа: 71
353
Введите порядковый номер искомого простого числа: 71
353
Введите порядковый номер искомого простого числа: 71
353
simple(10)         0.00055
simple(100)        0.06528
simple(1000)       9.99312      # (2) оказался самым лучшим по всем показателям
simple_2(10)       0.00120
simple_2(100)      0.85449
simple_2(300)    112.70226      # (1) отвратительный результат
simple_3(10)       0.00138
simple_3(100)      0.25015
simple_3(1000)    46.23899      # (3) нормальный результат

Выводы:
(1) даже при 300 итерациях алгоритм ужасен, зато лаконичен))
(2) оптимальный поскольку нет лишних вычислений
(3) результат не очень за счет О(n^2) сложности и излишних вычислений.
'''
