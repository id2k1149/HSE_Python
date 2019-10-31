# Частотный анализ
'''
Дан текст.
Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
Слова должны быть отсортированы по убыванию их количества появления в тексте,
а при одинаковой частоте появления — в лексикографическом порядке.

Указание.
После того, как вы создадите словарь всех слов, вам захочется отсортировать его
по частоте встречаемости слова. Желаемого можно добиться, если создать список,
элементами которого будут кортежи из двух элементов: частота встречаемости
слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')].
Тогда стандартная сортировка будет сортировать список кортежей,
при этом кортежи сравниваются по первому элементу,
а если они равны —то по второму. Это почти то, что требуется в задаче.

my_list = []
for key, value in my_dict.items():
    pair = (value, key)
    my_list.append(pair)

answer = sorted(my_list, reverse=True)
print(len(answer), answer)

Формат ввода
Вводится текст.
'''
in_file = open("input.txt")
text = in_file.read().split()
in_file.close()

my_dict = dict()
for word in text:
    my_dict[word] = my_dict.get(word, 0) + 1

for word in sorted(my_dict.items(), key=lambda x: (-x[1], x[0])):
    print(word[0])