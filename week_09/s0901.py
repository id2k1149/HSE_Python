# Класс
'''
Реализуйте класс Matrix. Он должен содержать:
Конструктор от списка списков.
Гарантируется, что списки состоят из чисел, не пусты и все имеют одинаковый
размер. Конструктор должен копировать содержимое списка списков,
т. е. при изменении списков, от которых была сконструирована матрица,
содержимое матрицы изменяться не должно.
Метод __str__, переводящий матрицу в строку.
При этом элементы внутри одной строки должны быть разделены знаками табуляции,
а строки — переносами строк. После каждой строки не должно быть символа
табуляции и в конце не должно быть переноса строки.
Метод size без аргументов, возвращающий кортеж вида
(число строк, число столбцов).
Пример теста с участием этого метода есть в следующей задаче этой недели.
'''
class Matrix:
    def __init__(self, i = 0, j = 0, x = 0):
        self.i = i
        self.j = j
        self.x = x
    def __str__(self):
        return


    def __size__(self):