# Задача 17. Сколько неповторющейся чисел в масиве
# [1,1,2,0,-1,3,4,4] -> 6

# Решение 1 через множество

list_1 = [1, 1, 2, 3, 0, -4, 4, 4]
print(len(set(list_1)))

# Решение 2

list_1 = [1, 1, 2, 2, 3, 3, 4, 4]
result_list = list()
for i in list_1:
  if i not in result_list:
    result_list.append(i)
print(result_list)
print(len(result_list))


