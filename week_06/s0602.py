# Сортировка
"""
Отсортируйте данный массив, используя встроенную сортировку.

Первая строка входных данных содержит количество элементов в массиве N, N ≤ 10⁵
Далее идет N целых чисел, не превосходящих по абсолютной величине 10⁹.
"""
n = int(input())
my_list = list(map(int, input().split()))
sorted_list = sorted(my_list)
print(*sorted_list)