# 33.Хакер Василий получил доступ к классному журналу и хочет заменить 
# все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.

# 5 -> 13334

# 13331

n = int(input())
list1 = list()
for i in range(n):
    x = int(input())
    list1.append(x)
print(list1)
# list1 = [int(input()) for i in range(int(input()))]

max_n = max(list1)
min_n = min(list1)

for i in range(len(list1)):
    if list1[i] == max_n:
        list1[i] = min_n

print(list1)
