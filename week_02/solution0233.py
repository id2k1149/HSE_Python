# Длина последовательности
'''
Программа получает на вход последовательность целых неотрицательных чисел,
каждое число записано в отдельной строке. Последовательность завершается
числом 0, при считывании которого программа должна закончить свою работу и
вывести количество членов последовательности (не считая завершающего числа 0).
Числа, следующие за числом 0, считывать не нужно.
'''
n = int(input())
if n != 0:
    i = 1
else:
    i = 0
while n != 0:
    n = int(input())
    if n != 0:
        i += 1
print(i)
