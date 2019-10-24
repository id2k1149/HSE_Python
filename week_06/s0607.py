# Результаты олимпиады
'''
В олимпиаде участвовало N человек. Каждый получил определенное количество
баллов, при этом оказалось, что у всех участников разное число баллов.
Упорядочите список участников олимпиады в порядке убывания набранных баллов.

Формат ввода
Программа получает на вход число участников олимпиады N. Далее идет N строк,
в каждой строке записана фамилия участника, затем, через пробел, набранное им
количество баллов.

Формат вывода
Выведите список участников (только фамилии) в порядке убывания набранных баллов
'''
n = int(input())
student_list = []
for i in range(n):
    name_points = input().split()
    student_data = (int(name_points[1]), name_points[0])
    student_list.append(student_data)
student_list.sort(reverse=True)
for i in range(len(student_list)):
    print(student_list[i][1])