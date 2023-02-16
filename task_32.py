# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from func_rndlist import new_list



list_1 = new_list(20,20,-20)
min_number = int(input('min '))
max_number = int(input('max '))
print(list_1)
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)