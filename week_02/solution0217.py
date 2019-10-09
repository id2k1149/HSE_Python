# Узник замка Иф
'''
За многие годы заточения узник замка Иф
проделал в стене прямоугольное отверстие размером D×E.
Замок Иф сложен из кирпичей, размером A×B×C.
Определите, сможет ли узник выбрасывать кирпичи в море
через это отверстие
(очевидно, стороны кирпича должны быть
параллельны сторонам отверстия).
'''
a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if a <= c <= b:
    x1 = a
    x2 = c
elif b <= a <= c:
    x1 = b
    x2 = a
elif b <= c <= a:
    x1 = b
    x2 = c
elif c <= a <= b:
    x1 = c
    x2 = a
elif c <= b <= a:
    x1 = c
    x2 = b
else:
    x1 = a
    x2 = b
if d <= e:
    y1 = d
    y2 = e
else:
    y1 = e
    y2 = d
if x1 <= y1 and x2 <= y2:
    print('YES')
else:
    print('NO')