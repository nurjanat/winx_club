x = 7
list1 = [1,2,3,4,5,6,7,7,7]
i = 0
len_list1 = len(list1)
while i < len_list1:
    if x in list1:
        list1.remove(x)
    i = i + 1
print(list1)