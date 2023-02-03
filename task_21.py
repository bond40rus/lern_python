

L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)


# Решение 2
list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
list_2 = list()
for i in list_1:
    for j in i:
        list_2.append(i[j])

list_result = list()
for i in list_2:
  if i not in list_result:
    list_result.append(i)
print(list_result)


# решение 3

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
set_1 = set()
for i in list_1:
    for j in i:
        set_1.add(i[j])
print(set_1)



