from random import randint


def rnd(maxnum: int):
    return randint(1, maxnum)

#############################
def new_list_sort(count: int, num: int):
    ls = []
    a = 0
    while a < count:
        ls.append(rnd(num))
        a += 1
    ls.sort()
    return ls

#############################
def new_list(count: int, num: int):
    ls = []
    a = 0
    while a < count:
        ls.append(rnd(num))
        a += 1
    return ls

#############################
def new_list_unic(count: int, num: int):
    if num < count: 
        num = count
    ls = []
    a = 0
    while a < count:
        if a == 0:
            ls.append(rnd(num))
            a += 1
        else:
            ls.append(rnd(num))
            a += 1
            i = 0
            while i < a-1:
                # print(ls[i], ls[a-1], ls[i] != ls[a-1], i, a-1)
                if ls[i] != ls[a-1]:
                    i += 1
                else:
                    ls.pop()
                    a -= 1
                    # print(ls)
                    break
        # print()
    # print()
    # ls.sort()
    return ls


##print(new_list_unic(10,100))

#############################
def creat_user_list(num: int):
    mass = []
    i = 0
    while i < num:
        try:
            n =  int(input(f'Введите елемент {i + 1} из {num} -> '))
        except:
            n = 0
        mass.append(n)
        i += 1
    return mass
