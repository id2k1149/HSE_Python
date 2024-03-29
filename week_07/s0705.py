# Угадай число
'''
Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
Беатриса пытается угадать это число, для этого она называет некоторые множества
натуральных чисел. Август отвечает Беатрисе YES, если среди названных ею чисел
есть задуманное или NO в противном случае. После нескольких заданных вопросов
Беатриса запуталась в том, какие вопросы она задавала и какие ответы получила и
просит вас помочь ей определить, какие числа мог задумать Август.

Формат ввода
Первая строка входных данных содержит число n — наибольшее число, которое мог
загадать Август. Далее идут строки, содержащие вопросы Беатрисы. Каждая строка
представляет собой набор чисел, разделенных пробелами.
После каждой строки с вопросом идет ответ Августа: YES или NO.
Наконец, последняя строка входных данных содержит одно слово HELP.

Формат вывода
Вы должны вывести (через пробел, в порядке возрастания) все числа,
которые мог задумать Август.
'''
n = int(input())
no_set = set()
i = 1
while True:
    input_line = input()
    if input_line == 'HELP':
        break
    else:
        input_set = set(map(int, input_line.split()))
        answer = input()
        if answer == "YES":
            if i == 1:
                yes_set = input_set
                i += 1
            else:
                yes_set &= input_set
                yes_set.discard(no_set)
        elif len(yes_set) == 1:
            break
        elif answer == "NO":
            no_set = no_set | input_set
            yes_set = yes_set - no_set
answer = sorted(yes_set)
print(*answer)
