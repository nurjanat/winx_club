str1 = "dict1 dict2 dict3"
print(str1.split())


list1 = ["dict1","dict2", "dict3", "dict4", "dict5","dictionary6"]
print(max(list1))
y = max(list1)
list1.remove(y)
print(list1)


str3 = "nurjaaaanaaaat"
a = 'a'
count_a = 0
for alpha in str3:
    if alpha == a:
        count_a += 1
if count_a == len(str3):
    print(True)
else:
    print(False)
