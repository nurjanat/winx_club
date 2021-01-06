list1 = [1,2,3,4,5,6,7,7,7,9,9,9,9]
x = 7
i = 0
count_7 = 0
len_(list1) = len(list1)
while i <  len(list1):
    if list1[i] == x:
        count_7 +=1
        list1.remove(x)
    i = i + 1
print(list1)


# i = 0
# x = 2
# count_2 = 0
# list2 = [1,2,2,2,3]
# def remove_x(x,list2):
#     while i < list2[i] == x:
#         count_2 +=1
#         list2.remove()
#     i = i + 1
# print(list2)
