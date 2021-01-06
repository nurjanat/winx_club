list1 = [1,2,3,4,5,6,7,8]
list2 = []
i = 1
while i < len(list1):
    if list1[i] % 2 == 0:
        list2.append(list1[i])
        print(list2)
    i = i + 1

