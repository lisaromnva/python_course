import database  


def txt_phon_dir(arg):
    phone_dir_txt = ''
    for i in arg:
        people = ''
        for j in i:
            people += j + ' ' 
        phone_dir_txt += people + '\n'
        # print(phone_dir_txt)
    return str(phone_dir_txt)