# Дробная часть
'''
Дано положительное действительное число X. Выведите его дробную часть.
'''
n = float(input())
x = n - int(n)
print('{0:.10}'.format(x))
