#  другая задача

n = int(input('Введите кол-во дней: '))
count = 0
max_count = 0
for i in range(n):
    temp = int(input())
    if temp > 0:
        count += 1
    else:
        if max_count < count:
            max_count = count
        count = 0
print(f'Результат {max_count}')
