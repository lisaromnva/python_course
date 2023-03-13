import database
import txt_dir
import databasetest

def data_coll():
    flag = True
    while flag:
        print("введите данные: ")
        data = [
            f'{int(databasetest.phone_dir[-1][0]) + 1}',
            input("фамилия: "),
            input("имя: "),
            input("отчество: "),
            input("телефон: ")]
        # return data
        i = 0
        while i < len(databasetest.phone_dir):
            if len(data[4]) != 12:  
                print('Не верно введен номер телефона, нужно 11 цифр, начиная с + ')
                break
            if data[1:] == databasetest.phone_dir[i][1:]:
                print('Данный абонент существует')
                a = input('Желаете выйти? \nДа - 1 \nНет - любой другой символ ')
                if a == '1':
                    flag = False
                    break
                break
            i += 1
            
        else:    
                  
            databasetest.phone_dir.append(data)
            
            f = open('HW_8\databasetest.py', 'w', encoding='utf-8')
            f.write(f'phone_dir = {databasetest.phone_dir}') 
            
            f.close()
            flag = False