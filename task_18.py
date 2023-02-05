# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

from func_rndlist import new_list

list_size = int(input('Введите размер листа -> '))
find_num = int(input('Какое число проверяем -> '))
temp_num = 1


ls = list(new_list(list_size, list_size))
min_num = list_size
res = ls[0]


for i in range(list_size):
    temp_num = find_num - ls[i]
    if temp_num > 0 and temp_num < min_num:
        res = ls[i]
        min_num = temp_num


print(f'{ls} -> {res}')
