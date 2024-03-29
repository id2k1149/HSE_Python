# Проверка числа на простоту
'''
Дано натуральное число n>1. Проверьте, является ли оно простым.
Программа должна вывести слово YES, если число простое и NO,
если число составное. Решение оформите в виде функции IsPrime(n),
которая возвращает True для простых чисел и False для составных чисел.
Программа должна иметь сложность O(корень из n): количество действий
в программе должно быть пропорционально квадратному корню из n (иначе говоря,
при увеличении входного числа в k раз, время выполнения программы должно
увеличиваться примерно в корень из k раз).
'''


def IsPrime(n):
    i = 2
    while n % i != 0 and i * i <= n:
        i += 1
    return i * i > n


n = int(input())
if IsPrime(n):
    print('YES')
else:
    print("NO")
