import databasetest


def del_subscriber():
    i = 0
    d = input("Введите id удаляемого абонента: ")
    while i < len(databasetest.phone_dir):
        if databasetest.phone_dir[i][0] == d:
            databasetest.phone_dir.pop(i)
            f = open('HW_8\databasetest.py', 'w', encoding='utf-8')
            f.write(f'phone_dir = {databasetest.phone_dir}') 
            f.close()
            print("Абонент удален")
            break
        i += 1
    else:
        print('Такого id нет ')