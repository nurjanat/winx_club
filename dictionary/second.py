# username = "nurjanat"
# password = "123456"
# def auth(check_user,check_pass):
#     if check_user == username and check_pass == password:
#         print("ok")
#     else:
#         print("not ok")


# auth(username,password)


# dict1 = {"phones":["iphone 6","iphone 7","iphone 8","iphone 10"],
#          "clothes":["jeans","cap","skirt","shirt"],
#          "food":["pizza","doner","hamburger"]
#          }

# dict1['phones'].append(4)
# print(dict1)
#




# list1 = ['iphone6','iphone7','coat','jeans','pizza','coca cola']



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
    if