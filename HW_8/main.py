import search
import data_collection
import txt_dir
import databasetest
import delit
import change


def menu_command():
    start = True
    while start:
        select = input(
        'Введите команду: \n'
        '(1) - найти абонента \n'
        '(2) - добавить абонента \n'
        '(3) - изменение данных абонента \n'
        '(4) - удаление абонента по id\n'
        '(5) - вывести на консоль весь справочник \n'
        '(6) - выйти из программы \n')
        
        if select == '1':
            search.search()
        elif select == '2':
            # Добавляет абонента в database с проверкой без id
            data_collection.data_coll() 
            
        elif select == '3':
            change.edit()

        elif select == '4':
            delit.del_subscriber()      
         
        elif select == '5':
            print(txt_dir.txt_phon_dir(databasetest.phone_dir))
            
        elif select == '6':
            start = False
            
        else:
            print("\nНЕ верная команда \n")
            
menu_command()