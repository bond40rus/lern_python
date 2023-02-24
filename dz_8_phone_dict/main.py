import json



def w_numbers():
    li = []
    flag = True
    count = 1
    while flag:
        print(f'Телефон {count}: ' , end='' )
        li.append(input('- > '))
        print(f'добавить еще номер да (yes) / нет (no) ? - > ',end='')
        if  input():
            count += 1           
        else:
            flag = False  
    return li



db_path = 'dz_8_phone_dict/phone_book.json'
welcome = 'Enter command: 1 - read & show | 2 - add record | 3 - search | 4 - delete contact DB | 5 - init DB | q - Quit\n'
phone_book = {
'test':{'phone': ['test'] , 'email':"test"}
}

def print_book(book):
    for k,v in book.items():
        print (k," - ", end = " | ")
        for i,j in v.items():
            print (i, j, end = " | ")
        print()

def save_db(path, db):
    with open(path, 'w', encoding='utf-8') as fh: # открываем файл на запись
        fh.write(json.dumps(db, ensure_ascii=False, indent=3))  #,indent=2 # преобразовываем словарь data в unicode-строку и записываем в файл
    print('БД успещно сохранена')

def load_db(path):
    with open(path,'r', encoding='utf-8') as fh:
        BD_local =json.load(fh)
    print('БД успешно загружена')
    return BD_local
        
def new_record(book):
    k= input('Введите ФИО - > ')
    a={}
    a['phone']=w_numbers()
    a['email']=input('Введите e-mail - > ')
    book[k]=a

def search_contact (file):
    with open(file) as json_file:
        data = dict(json.load(json_file))
        #print(type(data))
        find = input('Ищем контакт - > ')
        for k,i in data.items():
            if k == find:
                print(f'{k} - {i}')
                break


def delete_contact (file):
    with open(file) as json_file:
        data = dict(json.load(json_file))
        #print(type(data))
        find = input('удалить контакт - > ')
        data.pop(find,None)
        return data

action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        print_book(phone_book)
        print()
    elif action == '2':
        new_record(phone_book)
        print()
    elif action == '3':
        search_contact(db_path)
        print()
    elif action == '4':
        save_db(db_path, delete_contact(db_path))
        print()
    elif action == '5':
        save_db(db_path, phone_book)
        print()
save_db(db_path,phone_book)
