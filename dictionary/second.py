# username = "nurjanat"
# password = "123456"
# def auth(check_user,check_pass):
#     if check_user == username and check_pass == password:
#         print("ok")
#     else:
#         print("not ok")


# auth(username,password)

# /
# dict1 = {"phones":["iphone 6","iphone 7","iphone 8","iphone 10"],
#          "clothes":["jeans","cap","skirt","shirt"],
#          "food":["pizza","doner","hamburger"]
#          }

# dict1['phones'].append(4)
# print(dict1)
#




# list1 = ['iphone6','iphone7','coat','jeans','pizza','coca cola']
#


# for product in list1:
#     if product == 'iphone6' or product == 'iphone7' :
#         file1 = open('phone.txt','a')
#         file1.write(product)
#     elif product == 'coat' or product == 'jeans':
#         file2 = open('shop.txt','a')
#         file2.write(product)
#     else:
#         file3 = open('food.txt','a')
#         file3.write(product)




def register(username,email,password,check_password):
    list1 = []
    if len(username) > 8 and password == check_password:
        list1.append(username)
        list1.append(password)
    else:
        print('пароли не совпадают')

    return list1


result = register('maksim123','maxsims@gmail.com','123456','123456')
username = result[0]
password = result[1]

def signin(username,password):
    if username == username and password == password:
        print("успешно")
    else:
        print("провал")

signin('maksim123','123456')

product_list = ['iphone X','iphone Y','samsung galaxy 2','nokia 3','nokia 999',
                'nike boots', 'adidas boots', 'dior shirt', 'raben shirt',
                'adidas shirt', 'channel coat', 'wedding dress', 'gucci cloak',
                'adidas cloak']


def write_to(filename,product):
    file1 = open(filename,'a')
    file1.write(product +'\n')

for line in product_list:
    write_to('catalogue.txt',line)

file2 = open('catalogue.txt')
product_file = file2.readlines()


def sort():
    for product in product_list:
        if 'iphone' in product or 'samsung' in product or 'nokia' in product:
            write_to('phones.txt',product)
            # file1 = open('phones.txt','a')
            # file1.write(product + '\n')
        elif 'boots' in product:
            write_to('boots.txt',product)
            # file2 = open('boots.txt','a')
            # file2.write(product + '\n')
        elif 'shirt' in product or 'coat' in product or 'dress' in product:
            write_to('clothes.txt',product)
            # file3 = open('clothes.txt','a')
            # file3.write(product + '\n')
sort()



user_input = input()
if user_input == 'boots':
    file1 = open('boots.txt')
    print(file1.read())
elif user_input == 'phones':
    file1 = open('phones.txt')
    print(file1.read())
elif user_input == 'clothes':
    file1 = open('clothes.txt')
    print(file1.read())






