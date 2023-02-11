dict1 = {'Tom': {'English': 5, "Math": 5}, 'Red': {'English': 4, "Math": 4}}

print(dict1)
for i in dict1['Tom'].items():
    print(*i)
print()
print(dict1['Red']['Math'])

dict1.update({'Wer': {'English': 3, "Math": 3}})
print(dict1)

dict1['Tom'].update({'Trud': 6})
print(dict1)

dict1['Red']['Math'] = 5
print(dict1)
