# Четные индексы
'''
Выведите все элементы списка с четными индексами
(то есть A[0], A[2], A[4], ...).
Программа должна быть эффективной и не выполнять лишних действий!

Вводится список чисел. Все числа списка находятся на одной строке.
'''
numList = list(map(int, input().split()))
for i in range(len(numList)):
    if i % 2 == 0:
        print(numList[i], sep=' ', end=' ')