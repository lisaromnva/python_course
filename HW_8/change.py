import databasetest


def edit():
    a = input("Введите id абонента: ")
    for i in databasetest.phone_dir[:]:
        if a in i:
            print(f'Редактировать: {i} \n')
            flag = True
            while flag:
                print('Изменить Фамилию = 1 \n'
                'Изменить Имя = 2 \n'
                'Изменить Отчество = 3 \n'
                'Изменить телефон = 4 \n')
                n = int(input('Введите нужную цифру: '))
                if n == 1 or n == 2 or n == 3 or n == 4: 
                    x = input('Введите новый элемент: ')
                    i.pop(n)
                    i.insert(n, x)
                    print(i)
                    f = open('HW_8\databasetest.py', 'w', encoding='utf-8')
                    f.write(f'phone_dir = {databasetest.phone_dir}') 
                    f.close()
                    break
                else:
                    print('Не верно указан индекс элемента \n')
            break        