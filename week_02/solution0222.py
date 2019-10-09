# Котлеты
'''
На сковородку одновременно можно положить k котлет.
Каждую котлету нужно с каждой стороны обжаривать m минут непрерывно.
За какое наименьшее время удастся поджарить с обеих сторон n котлет?
'''
k, m, n = int(input()), int(input()), int(input())
if n < k:
    t = 2 * m
elif (2 * n) % k == 0:
    t = m * (2 * n // k)
else:
    t = m * ((2 * n // k) + 1)
print(t)