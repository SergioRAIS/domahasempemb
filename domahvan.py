s = int(input('Ввод сумм 2-х чисел \n'))
p = int(input('Ввод произведение чисел \n'))
for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(f'стартововое число ="{x}", след число ="{y}"')