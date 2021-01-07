def backpack(items_list:list):
    #items_list = ['potato','potato','milk']
    i = 0
    list2 = []
    while i < len(items_list):
        item_count =items_list.count(items_list[i])
        list2.append(item_count)
        i += 1
    max_list = max(list2)
    result_elem = items_list[list2.index(max_list)]

    j = 0
    while j < max_list - 1:
        j += 1
        #remove
        items_list.remove(result_elem)
    return result_elem,max_list,items_list
print(backpack(['potato','potato','milk','milk','milk','milk']))

#return хранить
# print просто выкидывает


