# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

num = int(input("Все целые степени двойки числа -> "))
st = 0

while 2**st < num:
    print(2**st, end=' ')
    st += 1


