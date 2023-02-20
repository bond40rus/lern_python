# Lambda функции
print('lambda  функции: ')
n = lambda a, b: a + b
print(n(5,10))

def math (fun, a, b):
    print(fun(a,b))

math(lambda a, b: a + b, 5, 45)


print()
print('Функция map(a,b) принимает 2 аргумента: 1 - функция 2 - где это функциия будет применятся')
# Функция map
list_1 = [i for i in range(1,20)]
print(list_1)
list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)
print('Вариант 2 p.s  функция split()  преобразовывает в список значение по разделителю (по умолчанию пробел)')
data = '211 34 56 32 1'
data = list(map(int, data.split()))
print(type(data), type(data[0]), data)


print()
# Функция filter
print('Filter на вход два оргумента: 1 - функция 2 - обьект,  будетет возвращать те обьекты когда 1 оргумент функции будет равнятся true')
print('возвращать ток те елементы которые на конце имеют цифру 5')
data_filter = [12, 65, 9, 175,36]
res = list(filter(lambda x: x % 10 == 5, data_filter))
print(res)

