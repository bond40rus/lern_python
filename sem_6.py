def div_list(number: int) -> dict:
    div_dict = {}
    for j in range(1, number):
        summa_div = 0
        for i in range(1, j):
            if j%i == 0:
                summa_div += i
        div_dict[j] = summa_div
    return div_dict

number = int(input('Введите предел: '))

div_dict = div_list(number)

for i in range(1,number):
    for j in range(i,number):
        if i == div_dict.get(j) and j == div_dict.get(i) and i != j:
            print(i, j)
