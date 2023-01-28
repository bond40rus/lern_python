#####################
# a = int(input())
# b = int(input())
# if a == b:
#     print(0)
# else:
#     print(a + b - 1)
################################

year = int(input('Введите год: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'Год {year} является високосным.')
else:
    print(f'Год {year} не является високосным.')

##############################
 