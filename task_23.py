

n = [0, -1, 5, 2, 3]
cnt = 0
list_1 = list()
for i in range(len(n) - 1):
    if n[i] < n[i + 1]:
        cnt += 1
        list_1.append((n[i], n[i + 1]))
print(f"{cnt}({', '.join([str(i[0]) + ' < ' + str(i[1]) for i in list_1])})")

