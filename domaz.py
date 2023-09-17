n = int(input('Ввод числа N:'))
i = 0
while 2 ** i <= n:
    print(f' двойка в степени {i} равна {2 ** i}')
    i += 1