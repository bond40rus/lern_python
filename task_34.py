# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам


#  Вариант 2  Посидел и подумал :)
mel2 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
gls = 'а'
print('Парам пам-пам' if len(set(map(lambda x: [x[i] if x[i] == gls else 0 for i in range(len(x))].count(gls), mel2.split()))) == 1 else 'Пам парам') 




# mel = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# gls = 'а'

# # Вариант 1 
# def fi(data: str , bukva: str):
#     res = 0
#     for i in range(len(data)):
#         if data[i] == bukva:
#             res += 1
#     return res


# mel = len(set(map(lambda x: fi(x,gls), mel.split()))) 
# print('Парам пам-пам' if mel == 1 else 'Пам парам' ) # читается так: 'Парам пам-пам' если mel равно 1, иначе 'Пам парам'

# print()
















