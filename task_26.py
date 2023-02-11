# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def degree(num:int,step:int):
    if step == 1:
        return num 
    return num * degree(num,step-1)
   
    
print(degree(int(input('Число -> ')),int(input('Степень -> '))))    

