file1 = open('cars.txt','r')
# r = read, w = write,a = append
# print(file1.write('657744364'))
# write удаляет все что уже есть в нашем файле и вставит что вы написаои в консоль
# \n new line


list1 = file1.readlines()
list1.append('maksimka')
list1.pop(3)
print(list1)




