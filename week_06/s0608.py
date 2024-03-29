# Проходной балл
'''
Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов в
виде ЕГЭ, каждый из них оценивается целым числом от 0 до 100 баллов. При этом
абитуриенты, набравшие менее 40 баллов (неудовлетворительную оценку) по любому
экзамену из конкурса выбывают. Остальные абитуриенты участвуют в конкурсе по
сумме баллов за три экзамена.

В конкурсе участвует N человек, при этом количество мест равно K. Определите
проходной балл, то есть такое количество баллов, что количество участников,
набравших столько или больше баллов не превосходит K, а при добавлении к ним
абитуриентов, набравших наибольшее количество баллов среди непринятых
абитуриентов, общее число принятых абитуриентов станет больше K.

Формат ввода
Программа получает на вход количество мест K. Далее идут строки с информацией
об абитуриентах, каждая из которых состоит из имени (текстовая строка
содержащая произвольное число пробелов) и трех чисел от 0 до 100, разделенных
пробелами.

Используйте для ввода файл input.txt с указанием кодировки utf8 (для создания
такого файла на своем компьютере в программе Notepad++ следует использовать
кодировку UTF-8 без BOM).

Формат вывода
Программа должна вывести проходной балл в конкурсе. Выведенное значение должно
быть минимальным баллом, который набрал абитуриент, прошедший по конкурсу.

Также возможны две ситуации, когда проходной балл не определен.
Если будут зачислены все абитуриенты, не имеющие неудовлетворительных оценок,
программа должна вывести число 0.
Если количество имеющих равный максимальный балл абитуриентов больше чем K,
программа должна вывести число 1.
Используйте для вывода файл output.txt с указанием кодировки utf8.

Предупреждение
Пожалуйста, тестируйте файловый ввод и вывод на своем компьютере. В этой задаче
слушатели часто получают ошибки вроде RE на первом тесте, протестировав у себя
с помощью консоли и просто заменив input() на чтение из файла перед сдачей.
К сожалению, такую замену не всегда удается сделать без ошибок, и решение
слушателей действительно перестает правильно работать даже на первом тесте.
'''

inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
k = int(inFile.readline())
all_students = inFile.readlines()
sum_list = []
for i in range(len(all_students)):
    sum_list.append(all_students[i].split(' '))
    sum_list[i][-1] = sum_list[i][-1].strip()
result_list = []
for i in range(len(sum_list)):
    sum_list[i][-1] = int(sum_list[i][-1])
    sum_list[i][-2] = int(sum_list[i][-2])
    sum_list[i][-3] = int(sum_list[i][-3])
    if sum_list[i][-1] < 40:
        continue
    elif sum_list[i][-2] < 40:
        continue
    elif sum_list[i][-3] < 40:
        continue
    else:
        student_sum = sum_list[i][-1] + sum_list[i][-2] + sum_list[i][-3]
        sum_list[i].insert(0, student_sum)
        result_list.append(sum_list[i])
result_list.sort(reverse=True)
points_list = []
for i in range(len(result_list)):
    points_list.append(result_list[i][0])
points_list = points_list[:k+1]
if len(points_list) <= k:
    answer = 0
elif points_list[k] < points_list[k-1]:
    answer = points_list[k-1]
elif points_list[k] == points_list[k-1]:
    element = points_list[k]
    sort_points_list = sorted(points_list)
    for point in sort_points_list:
        if point > element:
            answer = point
            break
        else:
            answer = 1
print(answer, file=outFile)
inFile.close()
outFile.close()
