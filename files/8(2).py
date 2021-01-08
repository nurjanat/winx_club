# list1 = [1,1,2,3,3,4,5,4,6,6,7,7,8,8,9,9]
# list2 = []
# i = 0
# while i < len(list1):
#     if list1[i] not in list2:
#         list2.append(list1[i])
#     i += 1
# print(list2)

# print(set(list1))


file1 = open('cars.txt')
list1 = file1.readlines()
i = 0
while i < len(list1):
    print(list1[i].strip())
    i += 1
