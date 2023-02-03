# Задача 19
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.
# Input:   [1, 2, 3, 4, 5] k = 3
# Output:  [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения списка или список задан изначально.

# решение 1
ls = [1,2,3,4,5]
k= 3
print (ls[k:] + ls[:k] ) 


# решение 2
list_1 = [1, 2, 3, 4, 5]
k = int(input())
k = k % len(list_1)
list_result = list()

for i in range(k):
    list_result.append(list_1[len(list_1) - k + i])

for i in range(len(list_1) - k):
    list_result.append(list_1[i])
print(list_result)



# Решение 3
lst = [1, 2, 3, 4, 5]
k = 2

for i in range(k):
    lst.insert(0, lst.pop(-1))
print(lst)




