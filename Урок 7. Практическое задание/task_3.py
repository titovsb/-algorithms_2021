"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.
"""

from collections import deque
from random import randint
from timeit import timeit

MIN, MAX = 0, 100


def count_sort(l: list) -> list:
    '''https://ru.wikipedia.org/wiki/Сортировка_подсчетом'''
    tmp = [0] * (max(l) + 1)
    for i in range(len(l)):
        tmp[l[i]] += 1
    posix = 0
    for num in range(len(tmp)):
        for idx in range(tmp[num]):
            l[posix] = num
            posix += 1
    return l


def mdn(m: int) -> int:
    l = deque(count_sort([randint(MIN, MAX) for _ in range(m * 2 + 1)]))
    print(l)
    while len(l) > 1:
        l.pop()
        l.popleft()
    return l[0]


def mdn2(m: int) -> int:
    l = [randint(MIN, MAX) for _ in range(m * 2 + 1)]
    print(l)
    # while len(l) != (m+1):
    while len(l) - 1 > m:
        l.remove(max(l))
    return max(l)


if __name__ == '__main__':
    m = int(input('Введите m: '))
    while m:
        median1 = mdn(m)
        print(f'Медиана1 {median1}')
        median2 = mdn2(m)
        print(f'Медиана2 {median2}')
        m = int(input('Введите m: '))

'''
Введите m: 4
[62, 27, 22, 43, 7, 34, 65, 23, 52]
Медиана1 34 Медиана2 34
Введите m: 2
[87, 7, 79, 73, 2]
Медиана1 73 Медиана2 73
Введите m: 0

Выводы:
1. алгоритмов сортировок МНОГО, некоторые из них шуточные (случайными перестановками), другие весьма 
эффективны даже на сравнительно больших массивах, например объединением
2. элемент m теоретически важен, но в алгоритме функции mdn() никак не может быть применим, во втором случае,
переписал алгоритм для его использования
3. замеры не производились исходя из условий задачи.

'''
