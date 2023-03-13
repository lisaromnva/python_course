import databasetest

def search():
    arg = input("Напишите искомые данные: ")
    print()
    match = 0
    for i in databasetest.phone_dir:
        # for j in range(len(i)):
        for j in i:
            # print(j.upper())
            # if arg == i[j]:
            if arg.upper() == j.upper():
                # match.append(i)
                print(i,'\n')
                match += 1
    if match == 0: 
        print('Такого абонента нет \n')