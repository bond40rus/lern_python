# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3

# -> 1

from random import randint


def rnd(maxnum: int):
    return randint(1, maxnum)


def new_list(count: int, num: int):
    ls = []
    a = 0
    while a < count:  
            ls.append(rnd(num))
            a += 1

    return ls


list_size = int(input('Введите размер листа -> '))
find_num = int(input('Какое число проверяем -> '))

ls = list(new_list(list_size, 10))
res = 0

for i in range(list_size):
    if ls[i] == find_num:
        res += 1

print(f'В списке {ls} число {find_num} повторяется {res} раз(а)')
