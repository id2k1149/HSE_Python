# Список степеней двойки
'''
По данному числу N распечатайте все целые степени двойки, не превосходящие N,
в порядке возрастания.Операцией возведения в степень пользоваться нельзя!
'''
n = int(input())
i = 0
result = 1
while result <= n:
    print(result, end=' ')
    result = result * 2
    i += 1