# x = 10
# i = 0 # количество дней
# while x < 100:
#     i += 1
#     x = x + x * 0,1
#     print("день номер:", i,"расстояние",x)

username = 'maksimka'
password = '123456'

def sign_in():
    tries = 0
    while tries < 3:
        check_username = input()
        check_password = input()
        if  check_username == username and check_password == password:
            print('вы успешно вошли')
            break
        else:
            print('вы ввели неверные данные')
            tries += 1
sign_in()


